## Import
from PyPDF2 import PdfFileReader

## Setup
pdf = PdfFileReader(open('test_pdf.pdf', "rb"))
info = pdf.getDocumentInfo()
number_of_pages = pdf.getNumPages()

## Extracting information
pdf_info = f"""
    Information about {info.title}:
    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {number_of_pages}
  """

print(pdf_info)
