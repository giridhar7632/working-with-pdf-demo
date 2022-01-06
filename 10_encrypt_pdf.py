## Import
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_reader = PdfFileReader("lorem.pdf")
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    pdf_writer.addPage(page)

# Encrypt the PDF file
pdf_writer.encrypt(user_pwd = "UserSecret", owner_pwd = "SuperSecret", use_128bit = True)

with open("encrypted_lorem_pdf.pdf", "wb") as f:
    pdf_writer.write(f)
