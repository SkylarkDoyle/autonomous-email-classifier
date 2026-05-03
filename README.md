---
title: Email Classifier
emoji: 📧
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---


# 📧 Autonomous Email Classifier

A lightweight, automated system that connects to the Gmail API to read an inbox, classifies messages using a pre-trained zero-shot Hugging Face model, and displays the categorized emails in a Gradio dashboard.

## ✨ Features

- **Gmail Integration:** Securely fetch unread emails using Google OAuth 2.0 Web Server flow.
- **Zero-Shot Classification:** Categorize emails dynamically without needing to fine-tune a model on specific tags.
- **Interactive UI:** View separated inboxes (Work, Personal, Finance, etc.) inside a clean Gradio tabbed interface.
- **Accuracy Tracking:** Built-in Scikit-Learn evaluation logic for benchmarking model performance against ground truth labels.

## 🛠️ Tech Stack

- **Frontend:** [Gradio](https://gradio.app/)
- **Authentication:** [Google Auth OAuthlib](https://google-auth-oauthlib.readthedocs.io/)
- **NLP/Inference:** [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Evaluation:** [Scikit-Learn](https://scikit-learn.org/)

## 🎓 What You Will Learn

- **Authenticating and fetching emails** dynamically using the Google Gmail API and OAuth 2.0.
- **Integrating and running** a pre-trained Hugging Face zero-shot classification model for natural language processing.
- **Designing and deploying** interactive web interfaces using Gradio, tailored for Hugging Face Spaces.
- **Evaluating model performance** and tracking accuracy metrics (like precision and recall) using Scikit-Learn.
- **Mounting Gradio on FastAPI** to build a robust hybrid application that safely handles custom OAuth routes alongside the UI.

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.9+
- A Google Cloud Project with the **Gmail API** enabled and OAuth 2.0 Client IDs configured for a Web application.

### 2. Installation

Clone the repository, set up a virtual environment, and install dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup

Download your OAuth 2.0 credentials from your Google Cloud Console and save the file as `client_secrets.json` (or `client_secret.json`) in the root directory of the project.

### 4. Run the App

```bash
python main.py
```

## 📖 Usage

1. Start the application locally.
2. Click the **Login with Google** link displayed in the UI.
3. Authorize the application and copy the URL you are redirected to.
4. Paste the URL into the **Paste Redirect URL here** textbox in the dashboard.
5. Click **Authenticate & Classify** and wait for the model to process your inbox.
6. Navigate through the generated tabs to view your sorted emails.

## ⚠️ Important Note

Because Hugging Face Spaces embeds Gradio inside an `iframe`, automatic OAuth redirects are often stripped of query parameters. This project uses a "paste the redirect URL" approach to ensure stable authentication across environments without requiring a complex backend server.
