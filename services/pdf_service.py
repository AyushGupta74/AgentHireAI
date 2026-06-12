import fitz


class PDFService:

    @staticmethod
    def extract_text(file):

        pdf = fitz.open(stream=file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text() # type: ignore

        pdf.close()

        return text