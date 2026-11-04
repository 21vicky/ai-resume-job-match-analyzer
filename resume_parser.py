
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):

    try:
        # Open the PDF file
        reader = PdfReader(pdf_path)

        # Store extracted text
        extracted_text = ""

        # Read every page
        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        return extracted_text

    except Exception as e:
        print("Error reading PDF:", e)
        return ""