from fastapi import HTTPException
from fastapi.responses import RedirectResponse
import gradio as gr

from fastapi import FastAPI, Request
from src.dashboard import Dashboard
from src.engine import EmailClassifier
from src.gmail_service import GmailService

# Create FastAPI app
app = FastAPI()

# Initialize services
gmail = GmailService()
engine = EmailClassifier()


@app.get("/login")
def login():
    """Redirects the user to the Google OAuth login page using get_auth_url()."""
    auth_url = gmail.get_auth_url()
    return RedirectResponse(url=auth_url)


@app.get("/oauth2callback")
def callback(request: Request):
    """Exchanges the authorization response for valid credentials and redirects to the dashboard."""
    full_url = str(request.url).replace("http://", "https://", 1)

    try:
        gmail.authenticate(full_url)
        return RedirectResponse(url="/")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Authentication failed: {str(e)}")


dashboard = Dashboard(gmail, engine).render()
app = gr.mount_gradio_app(app, dashboard, path="/")
