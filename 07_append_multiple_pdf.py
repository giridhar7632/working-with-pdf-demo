## Import
from PyPDF2 import PdfFileMerger

## Create a PDF merger object
pdf_merger = PdfFileMerger()

## Append the PDFs to the merger
pdf_merger.append("pdf_1.pdf")
pdf_merger.append("pdf_2.pdf")
pdf_merger.append("pdf_3.pdf")

## Write to file
with open("appended_pdf_123.pdf", "wb") as f:
    pdf_merger.write(f)
