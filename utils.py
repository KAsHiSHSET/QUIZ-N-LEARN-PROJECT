from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.

    Parameters:
        uploaded_file (BytesIO): The uploaded PDF file.

    Returns:
        str: The extracted text as a single string.
    """
    text = ""
    pdf_reader = PdfReader(uploaded_file)
    
    # Iterate through all pages in the PDF
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text
