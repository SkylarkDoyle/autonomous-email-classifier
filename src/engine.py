import pandas as pd
from transformers import pipeline
from sklearn.metrics import classification_report


class EmailClassifier:
    def __init__(self, model_name: str = "facebook/bart-large-mnli"):
        """Initializes the zero-shot classifier model"""
        self.classifier = pipeline("zero-shot-classification", model=model_name)

    def prepare_data(self, email_list: list[dict]) -> pd.DataFrame:
        """
        Converts a list of email dictionaries into a cleaned Pandas DataFrame.
        Should combine 'subject' and 'snippet' into a single text column.
        """
        df = pd.DataFrame(email_list)

        df["content"] = df["subject"] + " " + df["snippet"]
        return df[["content"]]

    def classify_emails(self, df: pd.DataFrame, candidate_labels: list[str]):
        """
        Runs the zero-shot classification on the DataFrame.
        """
        if candidate_labels is None:
            candidate_labels = [
                "Work",
                "Urgent",
                "Personal",
                "Finance",
                "Social",
                "Promotions",
                "Spam",
                "Others",
            ]

        texts = df["content"].tolist()

        results = self.classifier(texts, candidate_labels=candidate_labels)
        df["category"] = [res["labels"][0] for res in results]
        return df

    def evaluate(self, y_true: list[str], y_pred: list[str]) -> dict:
        """
        Calculates accuracy, precision, and recall using scikit-learn.
        Returns a dictionary of metrics.
        """
        report = classification_report(y_true, y_pred, output_dict=True)
        return report
