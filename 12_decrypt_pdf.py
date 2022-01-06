## Import
from PyPDF2 import PdfFileReader

## Get the encrypted file
pdf_reader = PdfFileReader("encrypted_lorem_pdf.pdf")

## Decrypt the file using password
pdf_reader.decrypt("SuperSecret")
print(pdf_reader.getPage(0).extractText())
