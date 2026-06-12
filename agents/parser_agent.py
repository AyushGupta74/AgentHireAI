from services.pdf_service import PDFService
from utils.preprocess import TextPreprocessor


class ResumeParserAgent:

    def parse_resume(self, file):

        raw_text = PDFService.extract_text(file)

        cleaned_text = TextPreprocessor.clean(raw_text)

        return cleaned_text
