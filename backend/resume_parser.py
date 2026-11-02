
from PyPDF2 import PdfReader
from docx import Document


ALLOWED_EXTENSIONS = {"pdf", "docx"}


def extract_resume_text(file):
    """
    Extract text from PDF or DOCX resume.
    """

    filename = file.filename

    if not filename or "." not in filename:
        raise ValueError("Invalid file name.")

    extension = filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Only PDF and DOCX files are supported.")

    try:
        if extension == "pdf":
            reader = PdfReader(file.stream)

            if reader.is_encrypted:
                raise ValueError("Password-protected PDFs are not supported.")

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

        elif extension == "docx":
            document = Document(file.stream)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        text = text.strip()

        if not text:
            raise ValueError(
                "No readable text found in the resume."
            )

        return text

    except ValueError:
        raise

    except Exception as error:
        raise ValueError(
            "Unable to read this resume. Please upload a valid document."
        ) from error
