## Import
from PyPDF2 import PdfFileMerger

## Create a PDF merger object
pdf_merger = PdfFileMerger()

## Append the PDFs to the merger
pdf_merger.append("pdf_1.pdf")

## Merge the second PDF file using index position and path
pdf_merger.merge(1, "pdf_2.pdf", pages=(1,3))  # pages = (start, stop)

## Write to file
with open("merged_pdf_range.pdf", "wb") as f:
    pdf_merger.write(f)
