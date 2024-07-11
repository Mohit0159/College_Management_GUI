import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from printoutpage import my_cust_PDF
class StudentReport1:
    def __init__(self,hwindow):
        # self.window = Tk()  # to create independent window
        self.window = Toplevel(hwindow) # to create child window (studentpage) of hwindow(homepage)

        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w-140  )
        h1 = int( h-150 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))  # (width,height,x,y)
        # --------------- background -----------------------
        from PIL import Image, ImageTk

        # ------------------------background image------------------------------

        self.bkimg1 = Image.open("myimages//teacher_bg.jpg").resize((w1, h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window, image=self.bkphotoimg1)
        self.bklbl.place(x=0, y=0)

        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Student Report ",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)


        self.b1 = Button(self.window,text="Print",font=myfont1,background=mycolor3,foreground=mycolor1,command=self.getPrintout)

        # ------------------- table ------------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8'],height=20)

        self.mytable.heading('c1',text="Roll no")
        self.mytable.heading('c2',text="Name")
        self.mytable.heading('c3',text="Phone")
        self.mytable.heading('c4',text="Gender")
        self.mytable.heading('c5',text="DOB")
        self.mytable.heading('c6',text="Address")
        self.mytable.heading('c7',text="Department")
        self.mytable.heading('c8',text="Course")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=150,anchor='center')
        self.mytable.column('c2',width=200,anchor='center')
        self.mytable.column('c3',width=150,anchor='center')
        self.mytable.column('c4',width=150,anchor='center')
        self.mytable.column('c5',width=150,anchor='center')
        self.mytable.column('c6',width=200,anchor='center')
        self.mytable.column('c7',width=150,anchor='center')
        self.mytable.column('c8',width=150,anchor='center')


        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)
        self.mytable.place(x=x1,y=y1)
        self.b1.place(x=x1+500,y=y1+500)


        self.makedatabaseConnection()
        self.getAllData()
        self.window.mainloop()
    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['Rollno', 'Name', 'Gender', 'Phone No', 'DOB', 'Address', 'Department', 'Course']
        pdf.print_chapter(self.pdata, headings)
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')



    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e),parent=self.window)


    def getAllData(self):
        try:
            #rollno	name	phone	gender	dob	address	department	course
            qry = "select * from student "
            rowcount = self.curr.execute(qry )
            data = self.curr.fetchall()
            self.pdata=[]
            if data:
                for myrow in data:
                    self.pdata.append(myrow[:-1])
                    # r1 = [myrow[0],myrow[1],myrow[2],myrow[3],myrow[4],myrow[5],myrow[6],myrow[7]]
                    # self.pdata.append(r1)
                    self.mytable.insert('',END,values=myrow)
            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyhomepage=Tk()
    StudentReport1(dummyhomepage)
    dummyhomepage.mainloop()
