import os
import json
from dotenv import load_dotenv
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

load_dotenv()


class GmailService:
    def __init__(self):
        """Initializes the service and configures the OAuth 2.0 flow"""
        config_str = os.environ.get("GOOGLE_CLIENT_SECRET")
        client_config = json.loads(config_str)
        self.scopes = ["https://www.googleapis.com/auth/gmail.readonly"]
        self.flow = Flow.from_client_config(
            client_config,
            scopes=self.scopes,
            redirect_uri="https://doyin14-email-classifier.hf.space/oauth2callback",
        )

    def get_auth_url(self):
        """Generates the authorization URL for the user to visit"""
        auth_url, _ = self.flow.authorization_url(prompt="consent")
        return auth_url

    def authenticate(self, auth_response_url: str, state: str = None):
        """Exchanges the authorization response for valid credentials"""
        if state:
            self.flow.state = state # Fixes the multi-worker crash

        self.flow.fetch_token(authorization_response=auth_response_url)
        creds = self.flow.credentials
        self.service = build("gmail", "v1", credentials=creds)

    def fetch_unread_emails(self, max_results: int = 50) -> list[dict]:
        """Fetches unread emails from the authenticated user's Gmail inbox"""
        if not hasattr(self, "service"):
            raise Exception("Service not authenticated. Please login first!")

        email_data = []

        def on_email_fetched(request_id, response, exception):
            if exception:
                return

            headers = response.get("payload", {}).get("headers", [])
            subject = next(
                (h["value"] for h in headers if h["name"] == "Subject"), "No Subject"
            )
            email_data.append(
                {"subject": subject, "snippet": response.get("snippet", "")}
            )

        try:
            # Get list of messages IDs
            results = (
                self.service.users()
                .messages()
                .list(userId="me", q="is:unread", maxResults=max_results)
                .execute()
            )
            messages = results.get("messages", [])

            #  Build and execute the batch
            batch = self.service.new_batch_http_request(callback=on_email_fetched)
            for msg in messages:
                batch.add(
                    self.service.users().messages().get(userId="me", id=msg["id"])
                )

            batch.execute()
            return email_data
        except HttpError as error:
            print(f"An error occurred: {error}")
