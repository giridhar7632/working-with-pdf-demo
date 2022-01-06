## Import
from fpdf import FPDF

## Create a new PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font("Arial", size=12)

## Open the .txt file in read mode
text = open("lorem_text.txt", "r")

## Loop through the lines in the text file and add them to the PDF
for line in text:
    pdf.cell(0, 5, txt=line, ln=1)

## Save the pdf file
pdf.output("lorem_pdf.pdf")
print("PDF created!")
