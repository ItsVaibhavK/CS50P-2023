from fpdf import FPDF


# user input
name = input("Name: ")
# by default, pdf = FPDF(orientation="P", unit="mm", format="A4")
# create object
pdf = FPDF()
# create blank page, disable page break
pdf.add_page()
pdf.set_auto_page_break(auto=False)
# set font
pdf.set_font("helvetica", "B", 50)
# make header with border, center-aligned
pdf.cell(0, 65, "CS50 Shirtificate", border=1, align="C")
# add in the shirt image
pdf.image("shirtificate.png", x=0.5, y=85)
# font size and color for text on shirt, and the text itself
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=41, y=150, txt=f"{name} took CS50")
# output pdf
pdf.output("shirtificate.pdf")
