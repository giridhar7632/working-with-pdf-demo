## Import
from PyPDF2 import PdfFileReader

## Create the PdfFileReader instance
pdf = PdfFileReader(open("lorem.pdf", "rb"))

## Create a new text file and open it in write mode
with open("lorem_text.txt", "w") as f:
  ## Loop through the PDF pages
    for page in pdf.pages:
        text = page.extractText()
      ## Write to the text file
        f.write(text)
