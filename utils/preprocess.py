import re


class TextPreprocessor:

    @staticmethod
    def clean(text):

        text = text.lower()

        text = re.sub(r'\n', ' ', text)

        text = re.sub(r'\t', ' ', text)

        text = re.sub(r'[^a-zA-Z\s]', ' ', text)

        text = re.sub(r'\s+', ' ', text)

        return text.strip()
