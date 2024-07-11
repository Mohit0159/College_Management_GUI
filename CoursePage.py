from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from PIL import Image,ImageTk


class CourseClass:
    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title('Course details page ')
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
        self.headlbl = Label(self.window,text="Course",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Course Name ",font=myfont1,background=mycolor1,foreground=mycolor2,width=10)
        self.L2 = Label(self.window,text=" Department",font=myfont1,background=mycolor1,foreground=mycolor2,width=10)
        self.L3 = Label(self.window,text="Duration",font=myfont1,background=mycolor1,foreground=mycolor2,width=10)
        self.L4 = Label(self.window,text="Fee ",font=myfont1,background=mycolor1,foreground=mycolor2,width=10)



        self.v1 = StringVar()
        self.c1 = Combobox(self.window, textvariable=self.v1, font=myfont1,state='readonly')

        self.t1 = Entry(self.window, font=myfont1)
        self.t3 = Entry(self.window,font=myfont1)
        self.v2 = StringVar()
        self.c2 = Combobox(self.window,values=["Years","Months","Weeks"],textvariable=self.v2,font=myfont1,state='readonly')

        self.t4 = Entry(self.window,font=myfont1)

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

        self.t1.bind("<FocusIn>", lambda e: self.myfocuscolor("t1", "yellow"))
        self.t1.bind("<FocusOut>", lambda e: self.myfocuscolor("t1", "white"))
        self.t3.bind("<FocusIn>", lambda e: self.myfocuscolor("t3", "yellow"))
        self.t3.bind("<FocusOut>", lambda e: self.myfocuscolor("t3", "white"))
        self.t4.bind("<FocusIn>", lambda e: self.myfocuscolor("t4", "yellow"))
        self.t4.bind("<FocusOut>", lambda e: self.myfocuscolor("t4", "white"))


        # ------------------- table ------------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2','c3','c4','c5'],height=18)

        self.mytable.heading('c1',text="Course")
        self.mytable.heading('c2',text="Department")
        self.mytable.heading('c3',text="Duration")
        self.mytable.heading('c4',text="Units")
        self.mytable.heading('c5',text="Fee")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=150,anchor='center')
        self.mytable.column('c2',width=150,anchor='center')
        self.mytable.column('c3',width=100,anchor='center')
        self.mytable.column('c4',width=100,anchor='center')
        self.mytable.column('c5',width=150,anchor='center')

        self.mytable.bind("<ButtonRelease>",lambda e : self.getTableData())

        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 150
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        self.b4.place(x=x1+x_diff*3,y=y1,width=120,height=30)
        self.mytable.place(x=x1+x_diff*3+200,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        self.b5.place(x=x1+x_diff*3,y=y1,width=120,height=30)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1,width=100)
        self.c2.place(x=x1+x_diff+x_diff-40,y=y1,width=140)
        y1+=y_diff
        self.L4.place(x=x1,y=y1)
        self.t4.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=120,height=40)
        self.b2.place(x=x1+x_diff,y=y1,width=120,height=40)
        self.b3.place(x=x1+x_diff+x_diff,y=y1,width=120,height=40)
        y1 += y_diff
        self.b6.place(x=x1, y=y1, width=350, height=40)



        self.makedatabaseConnection()
        self.getAllDepartments()
        self.clearPage()
        self.window.mainloop()
    def myfocuscolor(self, name, color_name):
        if name == "t1":
            self.t1.config(background=color_name)
        elif name == "t3":
            self.t3.config(background=color_name)
        else:
            self.t4.config(background=color_name)

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
            qry = "insert into course values(%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.v1.get(),self.t3.get(),
                    self.v2.get(), self.t4.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Course Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def updateData(self):
        if self.validate_check() == False:
            return
        try:
            #dname	cname	duration	time_unit	fee
            qry = "update course set department_name=%s, duration=%s, time_units=%s, fee=%s where course_name=%s"
            rowcount = self.curr.execute(qry , (self.v1.get(), self.t3.get(), self.v2.get(), self.t4.get(), self.t1.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success","Course Record Updated Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Updation \n"+str(e),parent=self.window)
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ?? ",parent=self.window)
        if ans=="yes":
            try:
                qry = "delete from course where course_name=%s"
                rowcount = self.curr.execute(qry , (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","Course Record Deleted Successfully",parent=self.window)
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
            selected_course = self.t1.get()
        else:
            selected_course=pk_col
        try:
            qry = "select * from course where course_name=%s"
            rowcount = self.curr.execute(qry , (selected_course))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.v1.set(data[1])
                self.t3.insert(0,data[2])
                self.v2.set(data[3])
                self.t4.insert(0,data[4])

            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def clearPage(self):
        self.t1.delete(0,END)
        self.c1.set("Choose Department")
        self.t3.delete(0,END)
        self.c2.set("Units")
        self.t4.delete(0,END)
        self.getAllData()



    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())
            dept_name = self.v1.get()
            if dept_name=="Choose Department":
                dept_name=""
            qry = "select * from course where department_name like %s "
            rowcount = self.curr.execute(qry ,(dept_name+"%"))
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
            messagebox.showwarning("Validation Check", "Enter Course name  ", parent=self.window)
            return False
        if (self.v1.get() == "Choose Department") or (self.v1.get() == "No Department"):
            messagebox.showwarning("Input Error", "Please Select Department ", parent=self.window)
            return False
        elif not (self.t3.get().isdigit()) or len(self.t3.get()) <1:
            messagebox.showwarning("Validation Check", "Enter valid duration", parent=self.window)
            return False
        elif (self.v2.get() == "Units") :
            messagebox.showwarning("Input Error", "Please Select Time_Units ", parent=self.window)
            return False
        elif not (self.t4.get().isdigit()):
            messagebox.showwarning("Validation Check", "Invalid Fees", parent=self.window)
            return False
        return True


    def getAllDepartments(self):
        try:
            qry = "select * from department "
            rowcount = self.curr.execute(qry )
            data = self.curr.fetchall()
            self.deptList=[]
            if data:
                self.c1.set("Choose Department")
                for myrow in data:
                    self.deptList.append(myrow[0])
            else:
                self.c1.set("No Department")

            self.c1.config(values = self.deptList)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyhomepage=Tk()
    CourseClass(dummyhomepage)
    dummyhomepage.mainloop()
