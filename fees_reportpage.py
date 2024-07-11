import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

from printoutpage import my_cust_PDF


class FeeReportPage2:
    def __init__(self,hwindow):
        # self.window = Tk()  # to create independent window
        self.window = Toplevel(hwindow) # to create child window (studentpage) of hwindow(homepage)
        self.window.title('Fee Report Detail')
        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w-140  )
        h1 = int( h-150 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))  # (width,height,x,y)

        #--------------- background -----------------------
        from PIL import Image,ImageTk

        self.bkimg1 = Image.open("myimages//teacher_bg.jpg").resize((w1,h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window,image=self.bkphotoimg1)
        self.bklbl.place(x=0,y=0)

        # ------------------------------------------------------
        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Fee Report ",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)

        self.l1=Label(self.window,text="Select Rollno",font=myfont1,background=mycolor3,foreground=mycolor1)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v1,font=myfont1,state='readonly')
        self.c1.bind("<<ComboboxSelected>>",lambda e : self.getAllData())


        self.b1 = Button(self.window,text="Print",font=myfont1,background=mycolor3,foreground=mycolor1,command=self.getPrintout)

        # table---------------------
        self.mytable = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4'], height=15)

        self.mytable.heading('c1', text="Roll no")
        self.mytable.heading('c2', text="Name")
        self.mytable.heading('c3', text="Payment date")
        self.mytable.heading('c4', text=' Paid Fees')

        # self.mytable.heading('c7', text="Payment Mode")
        # self.mytable.heading('c8', text="Payment Amount")

        self.mytable['show'] = 'headings'

        self.mytable.column('c1', width=170, anchor='center')
        self.mytable.column('c2', width=190, anchor='center')
        self.mytable.column('c3', width=200, anchor='center')
        self.mytable.column('c4', width=180, anchor='center')


        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff =200
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)
        self.l1.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.mytable.place(x=x1,y=y1)
        self.b1.place(x=x1 + 500, y=y1 + 500)

        self.makedatabaseConnection()
        self.getAllrollno()
        self.getAllData()
        # self.b1['state']='disable'
        self.window.mainloop()
    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['Rollno', 'Name', 'Payment Date',  'Paid fees']
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
            self.mytable.delete(*self.mytable.get_children())
            # rollno	name	phone	gender	dob	address	department	course
            qry = "select * from fee_detail where rollno=%s"
            rowcount = self.curr.execute(qry, (self.v1.get()))
            data = self.curr.fetchall()
            self.pdata=[]
            if data:
                for myrow in data:
                    r1 = [myrow[0],myrow[1],myrow[2],myrow[3]]
                    self.pdata.append(r1)
                    self.mytable.insert('', END, values=myrow)
                    # self.b1['state'] = 'normal'
            else:
                messagebox.showinfo("Empty", "No Record Found", parent=self.window)
                # self.b1['state'] = 'disable'
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion \n" + str(e), parent=self.window)

    def getAllrollno(self):
        try:
            qry = "select * from student "
            rowcount = self.curr.execute(qry )
            data = self.curr.fetchall()
            self.rollnolist=[]
            if data:
                self.c1.set("Choose rollno")
                for myrow in data:
                    self.rollnolist.append(myrow[0])
            else:
                self.c1.set("No rollno")

            self.c1.config(values = self.rollnolist)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)



if __name__ == '__main__':
    dummyhomepage=Tk()
    FeeReportPage2(dummyhomepage)
    dummyhomepage.mainloop()
