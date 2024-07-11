import os
from fpdf import FPDF
company="GNDU RC JAL. "
address="LADHEWALI"

class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(203, 23, 23)
        self.set_font('Helvetica', 'B', 20)
        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, company)
        self.ln(10) # line break

        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, address)
        self.ln(10)


        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'B', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    def chapter_content(self,data,headings):
        self.set_fill_color(200, 220, 255)
        self.ln()
        self.ln()
        self.set_font('Arial', 'B', 11)
        spacing=2
        total_cols = len(headings)
        col_width = self.w / (total_cols +1)


        row_height = self.font_size+2

        for i in headings:
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)
        self.set_font('Arial', '', 5)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        self.ln()
        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '(---------------------  end of page  -----------------------)'
        w = self.get_string_width(text1) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 6, text1)
    def print_chapter(self,data,headings):
        self.add_page()
        self.chapter_content(data,headings)

if __name__ == '__main__':
    pdf = my_cust_PDF()
    data=[['Rollno1','Name1','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno2','Name2','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno3','Name3','Gender','Phone No','Address','Department','Course','DOB']]

    headings = ['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB']
    pdf.print_chapter(data,headings)
    pdf.output('pdf_file1.pdf')
    os.system('explorer.exe "pdf_file1.pdf"')