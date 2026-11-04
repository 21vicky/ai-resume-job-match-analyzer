
from resume_parser import extract_text_from_pdf

pdf_path = input("Enter your PDF file path: ")

resume_text = extract_text_from_pdf(pdf_path)

if resume_text:
    print("\n===== EXTRACTED RESUME TEXT =====")
    print(resume_text)
else:
    print("No readable text found in the PDF.")
