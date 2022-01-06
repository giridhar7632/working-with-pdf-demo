## Import
from fpdf import FPDF

## Create a new PDF file
## Orientation: P = Portrait, L = Landscape
## Unit = mm, cm, in
## Format = 'A3', 'A4' (default), 'A5', 'Letter', 'Legal', custom size with (width, height)
pdf = FPDF(orientation="P", unit="mm", format="A4")

## Add a page
pdf.add_page()

## Specify Font
## Font Family: Arial, Courier, Helvetica, Times, Symbol
## Font Style: B = Bold, I = Italic, U = Underline, combinations (i.e., BI, BU, etc.)
pdf.set_font("Arial", size=18)
pdf.set_text_color(0, 0, 255)

## Add text
## Cell(w, h, txt, border, ln, align)
## w = width, h = height
## txt = your text
## ln = (0 or False; 1 or True - move cursor to next line)
## border = (0 or False; 1 or True - draw border around the cell)
pdf.cell(200, 10, txt="Hello World!", ln=1, align="C")

pdf.set_font("Arial", size=12)
pdf.set_text_color(0, 0, 0)
pdf.cell(200, 10, txt="This pdf is created using FPDF in Python.", ln=3, align="C")

## Add image
## name = Path or URL of the image
## x = x-coordinate, y = y-coordinate (default = None)
## w = width, h = height (If not specified or equal to zero, they are automatically calculated.)
## type = Image format. JPG, JPEG, PNG and GIF (If not specified, the type is inferred from the file extension.).
pdf.image(name="boy_night.jpg", h=107, type="JPG")

## Output the PDF
pdf.output("test_pdf.pdf")
print("pdf has been created successfully....")
