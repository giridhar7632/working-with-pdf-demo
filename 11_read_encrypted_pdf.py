## Import
from PyPDF2 import PdfFileReader

## Get the encrypted file
pdf_reader = PdfFileReader("encrypted_lorem_pdf.pdf")
pdf_reader.getPage(0)