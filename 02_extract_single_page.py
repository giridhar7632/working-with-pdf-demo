## Import
from PyPDF2 import PdfFileReader

## Create the PdfFileReader object
pdf = PdfFileReader(open("test_pdf.pdf", "rb"))

## Get the page object and extract the text
page_object = pdf.getPage(0) # page number starts from 0 (0-index)
text = page_object.extractText()

## Print the text
print(text)