## Import
from PyPDF2 import PdfFileReader, PdfFileWriter

## Create the PdfFileReader instance and Create a new PDF file using PdfFileWriter
old_pdf = PdfFileReader(open("lorem.pdf", "rb"))
new_pdf = PdfFileWriter()

## Loop through the pages and add them to the new PDF file
for page in old_pdf.pages[1:4]: # [1:4] means from page 1 to page 3
    new_pdf.addPage(page)

## Save the new PDF file
with open("new_lorem_pdf.pdf", "wb") as f:
    new_pdf.write(f)

