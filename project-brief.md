# Project Brief: Autonomous Email Classifier

## Goal
Build an automated system that connects to the Gmail API to read an inbox, classifies the messages using a pre-trained zero-shot Hugging Face model, and displays the categorized emails in a Gradio dashboard deployed on Hugging Face Spaces.

## Architecture & Tech Stack
*   **Data Source:** Google Mail API.
*   **Authentication:** `google-auth-oauthlib` (Web Server Flow) to allow dynamic, in-memory credential generation without storing user tokens on disk.
*   **Data Pipeline:** `pandas` to structure raw JSON email payloads into a tabular format.
*   **Intelligence:** Free, pre-trained Hugging Face zero-shot classification model.
*   **Evaluation:** `scikit-learn` for calculating accuracy metrics (precision, recall) against a test batch.
*   **Frontend & Hosting:** Gradio UI, hosted on Hugging Face Spaces.

## Build Order
1. **Authentication & Data Fetching:** Implement Google OAuth2 web server flow to authenticate users dynamically and fetch a batch of their emails via the Gmail API.
2. **Data Processing:** Structure the fetched emails into a Pandas DataFrame.
3. **Inference Engine:** Integrate the Hugging Face zero-shot classification pipeline.
4. **Evaluation Logic:** Add Scikit-learn metrics to measure classification accuracy.
5. **UI & Deployment:** Wrap the pipeline in a Gradio interface allowing users to log in, view categories in tabs, and deploy to HF Spaces.

## Key Risks
*   **Credential Security & Session Management:** Properly managing the Google OAuth state and redirect flow within a Gradio app hosted on HF Spaces, ensuring tokens are kept in memory and not leaked.
