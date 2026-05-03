import gradio as gr


class Dashboard:
    def __init__(self, gmail_service, classifier_engine):
        # State is safely stored here
        self.gmail = gmail_service
        self.engine = classifier_engine

    def _fetch_and_sort(self):
        """Helper method: Fetches, formats, classifies, and filters."""
        raw_messages = self.gmail.fetch_unread_emails()
        structured_inbox = self.engine.prepare_data(raw_messages)
        categorized_inbox = self.engine.classify_emails(structured_inbox, None)

        work_df = categorized_inbox[categorized_inbox["category"] == "Work"]
        urgent_df = categorized_inbox[categorized_inbox["category"] == "Urgent"]
        personal_df = categorized_inbox[categorized_inbox["category"] == "Personal"]
        finance_df = categorized_inbox[categorized_inbox["category"] == "Finance"]
        social_df = categorized_inbox[categorized_inbox["category"] == "Social"]
        promotions_df = categorized_inbox[categorized_inbox["category"] == "Promotions"]
        spam_df = categorized_inbox[categorized_inbox["category"] == "Spam"]
        others_df = categorized_inbox[categorized_inbox["category"] == "Others"]

        return (
            work_df,
            urgent_df,
            personal_df,
            finance_df,
            social_df,
            promotions_df,
            spam_df,
            others_df,
        )

    def refresh_data(self):
        """Triggered by the Refresh button."""
        return self._fetch_and_sort()

    def render(self):
        with gr.Blocks() as demo:
            gr.Markdown("# AI Inbox Classifier")

            with gr.Row():
                gr.HTML(
                    '<a href="/login" target="_blank" style="font-size: 16px; font-weight: bold; text-decoration: underline; color: #2563eb;">Click here to Login with Google</a>'
                )
                refresh_btn = gr.Button("Refresh Inbox")

            with gr.Tabs():
                with gr.Tab("Work"):
                    work_df = gr.DataFrame()
                with gr.Tab("Urgent"):
                    urgent_df = gr.DataFrame()
                with gr.Tab("Personal"):
                    personal_df = gr.DataFrame()
                with gr.Tab("Finance"):
                    finance_df = gr.DataFrame()
                with gr.Tab("Social"):
                    social_df = gr.DataFrame()
                with gr.Tab("Promotions"):
                    promotions_df = gr.DataFrame()
                with gr.Tab("Spam"):
                    spam_df = gr.DataFrame()
                with gr.Tab("Others"):
                    others_df = gr.DataFrame()

            refresh_btn.click(
                fn=self.refresh_data,
                inputs=[],
                outputs=[
                    work_df,
                    urgent_df,
                    personal_df,
                    finance_df,
                    social_df,
                    promotions_df,
                    spam_df,
                    others_df,
                ],
            )

            demo.load(
                fn=self.refresh_data,
                inputs=[],
                outputs=[
                    work_df,
                    urgent_df,
                    personal_df,
                    finance_df,
                    social_df,
                    promotions_df,
                    spam_df,
                    others_df,
                ],
            )

        return demo
