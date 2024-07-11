from tkinter import *
from tkinter import messagebox

from tkinter.ttk import Treeview
import pymysql
from PIL import Image,ImageTk


class DepartmentClass:
    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title('Department information page ')
        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w-140  )
        h1 = int( h-150 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))  # (width,height,x,y)
        # ------------------------background image------------------------------

        self.bkimg1 = Image.open("myimages//course_bg.jpg").resize((w1, h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window, image=self.bkphotoimg1)
        self.bklbl.place(x=0, y=0)

        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Department ",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Department Name ",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L2 = Label(self.window,text="Head Of Department ",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.l3=Label(self.window,text="Phone Number ",background=mycolor1,foreground=mycolor2,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1)
        self.t3=Entry(self.window,font=myfont1)
        self.t1.bind("<FocusIn>", lambda e: self.myfocuscolor("t1", "yellow"))
        self.t1.bind("<FocusOut>", lambda e: self.myfocuscolor("t1", "white"))
        self.t2.bind("<FocusIn>", lambda e: self.myfocuscolor("t2", "yellow"))
        self.t2.bind("<FocusOut>", lambda e: self.myfocuscolor("t2", "white"))
        self.t3.bind("<FocusIn>",lambda e: self.myfocuscolor("t3","yellow"))
        self.t3.bind("FocusOut",lambda e:self.myfocuscolor("t3","white"))


        self.b1 = Button(self.window,text="Save",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.saveData)
        self.b2 = Button(self.window,text="Update",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.updateData)
        self.b3 = Button(self.window,text="Delete",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.deleteData)
        self.b4 = Button(self.window,text="Fetch",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.fetchData)
        self.b5 = Button(self.window,text="Search",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.getAllData)
        self.b6 = Button(self.window, text="Clear All Entry Field", font=myfont1,
                         background=mycolor3, foreground=mycolor1, command=self.clearPage)



        # ------------------- table ------------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2',"c3"],height=20)

        self.mytable.heading('c1',text="Department Name")
        self.mytable.heading('c2',text="Head Of Department")
        self.mytable.heading("c3",text="P N")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=235,anchor='center')
        self.mytable.column('c2',width=235,anchor='center')
        self.mytable.column("c3",width=235,anchor="center")

        self.mytable.bind("<ButtonRelease>",lambda e : self.getTableData())

        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 180
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff+50,y=y1)
        self.b4.place(x=x1+x_diff*3-40,y=y1,width=120,height=30)
        self.mytable.place(x=x1+x_diff*3+83,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff+50,y=y1)
        self.b5.place(x=x1+x_diff*3-40,y=y1,width=120,height=30)
        y1+=y_diff
        self.l3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff+50,y=y1)
        y1 += y_diff
        self.b1.place(x=x1,y=y1,width=120,height=40)
        self.b2.place(x=x1+x_diff-20,y=y1,width=120,height=40)
        self.b3.place(x=x1+x_diff+x_diff-20,y=y1,width=120,height=40)
        y1 += y_diff
        self.b6.place(x=x1, y=y1, width=230, height=40)

        self.makedatabaseConnection()
        self.clearPage()
        self.window.mainloop()

    def myfocuscolor(self, name, color_name):
        if name == "t1":
            self.t1.config(background=color_name)
        else:
            self.t2.config(background=color_name)

    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e),parent=self.window)
    def saveData(self):
        if self.validate_check()==False:
            return

        try:

            qry = "insert into department values(%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get(),self.t3.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Department Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def updateData(self):
        if self.validate_check()==False:
            return

        try:

            qry = "update department set head_of_department=%s ,phone_number=%s where department_name=%s"

            rowcount = self.curr.execute(qry , (self.t2.get(),self.t3.get() ,self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Department Updated Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Updation \n"+str(e),parent=self.window)
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ?? ",parent=self.window)
        if ans=="yes":

            try:

                qry = "delete from department where department_name=%s"
                rowcount = self.curr.execute(qry , (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","Department Deleted Successfully",parent=self.window)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error","Error while Deletion \n"+str(e),parent=self.window)
    def getTableData(self):
        rowid = self.mytable.focus()
        tabledata = self.mytable.item(rowid)
        selectedRowdata = tabledata['values']
        col0 = selectedRowdata[0]
        self.fetchData(col0)
    def fetchData(self,pk_col=None):
        if pk_col==None:
            dept_name = self.t1.get()
        else:
            dept_name=pk_col
        try:
            qry = "select * from department where department_name=%s"
            rowcount = self.curr.execute(qry , (dept_name))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.getAllData()
    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())
            qry = "select * from department where head_of_department like %s "
            rowcount = self.curr.execute(qry ,(self.t2.get()+"%"))
            data = self.curr.fetchall()
            if data:
                for myrow in data:
                    self.mytable.insert('',END,values=myrow)
            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)

    def validate_check(self):
        if len(self.t1.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter department name  ", parent=self.window)
            return False
        elif len(self.t2.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter Head Of Department", parent=self.window)
            return False
        return True

if __name__ == '__main__':
    dummyhomepage=Tk()
    DepartmentClass(dummyhomepage)
    dummyhomepage.mainloop()










