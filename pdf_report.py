import argparse

def pdf(ppath):
    from fpdf import FPDF
    import csv
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(6)
    pdf.cell(0, 25, "Facebook Scraping", align="C")
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0)
    pdf.ln(40)
    pdf.set_font('Arial', 'B', 16)

    pdf.text(10, 50, '3- Analyse des données')
    pdf.ln(5)

    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 1.0, 'mean,max,min reacts and comments', align='C')
    pdf.ln(4)

    col_width = page_width / 4

    pdf.ln(4)

    th = pdf.font_size
    with open(ppath+"/table1.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pdf.set_font('Courier', 'B', 12)
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.set_font('Courier', '', 12)
            pdf.cell(col_width, th, row[1], border=1)
            pdf.cell(col_width, th, row[2], border=1)
            pdf.cell(col_width, th, row[3], border=1)
            pdf.ln(th)

    pdf.ln(10)
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'best 3 posts', align='C')
    pdf.ln(4)

    col_width = page_width / 4
    pdf.ln(4)

    th = pdf.font_size
    with open(ppath+'/max.csv', newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            pdf.set_font('Courier', '', 12)
            pdf.cell(col_width, th, row[1], border=1)
            pdf.cell(20, th, row[2], border=1)
            pdf.cell(40, th, row[3], border=1)
            pdf.cell(25, th, row[4], border=1)
            pdf.ln(th)

    pdf.ln(10)
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'Worst 3 posts', align='C')
    pdf.ln(5)

    col_width = page_width / 4
    pdf.ln(5)

    th = pdf.font_size
    with open(ppath+'/min.csv', newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            pdf.set_font('Courier', '', 12)
            pdf.cell(col_width, th, row[1], border=1)
            pdf.cell(20, th, row[2], border=1)
            pdf.cell(40, th, row[3], border=1)
            pdf.cell(25, th, row[4], border=1)
            pdf.ln(th)

    pdf.ln(10)
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'Most missing data', align='C')
    pdf.ln(5)

    col_width = page_width / 4
    pdf.ln(5)

    th = pdf.font_size
    with open(ppath+'/missingdata.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pdf.set_font('Courier', 'B', 12)
            pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.set_font('Courier', '', 12)
            pdf.cell(col_width, th, row[1], border=1)

            pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'Distribution of reactions', align='C')

    pdf.image(ppath+'/plot1.jpeg', x=10, y=210, w=80, h=80)
    pdf.image(ppath+'/plot2.jpeg', x=110, y=210, w=80, h=80)
    pdf.output(ppath+'/report.pdf')
    print('report is DONE')

parser = argparse.ArgumentParser(description='report')
parser.add_argument('ppath', type=str, help='ppath')
args = parser.parse_args()

if __name__=='__main__':
    print(pdf(args.ppath))