from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
from PIL import Image,ImageTk
class StudentClass:
    default_img_name = "defaultimage.jpg"
    def __init__(self,hwindow):
        # self.window = Tk()  # to create independent window
        self.window = Toplevel(hwindow) # to create child window (studentpage) of hwindow(homepage)
        self.window.title('Student detail page ')

        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w-140  )
        h1 = int( h-150 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))  # (width,height,x,y)


        #--------------- background -----------------------
        from PIL import Image,ImageTk

        # ------------------------background image------------------------------

        self.bkimg1 = Image.open("myimages//student_bg.jpg").resize((w1,h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window,image=self.bkphotoimg1)
        self.bklbl.place(x=0,y=0)


        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Student ",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Roll no ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L2 = Label(self.window,text="Name ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L3 = Label(self.window,text="Phone ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L4 = Label(self.window,text="Gender ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L5 = Label(self.window,text="DOB ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L6 = Label(self.window,text="Address ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L7 = Label(self.window,text="Department ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)
        self.L8 = Label(self.window,text="Course ",font=myfont1,background=mycolor1,foreground=mycolor2,width=9)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1)
        self.t3 = Entry(self.window,font=myfont1)
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window,text="Male",value="Male",variable=self.v1,background=mycolor1,font=myfont1)
        self.r2 = Radiobutton(self.window,text="Female",value="Female",variable=self.v1,background=mycolor1,font=myfont1)
        self.t5 = DateEntry(self.window,  background='darkblue',font=myfont1,
                    foreground='white', borderwidth=2, year=2000,date_pattern='y-mm-dd')
        self.t6 = Text(self.window,font=myfont1,width=20,height=3)
        self.v2 = StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v2,font=myfont1,state='readonly')
        # self.c1.bind("<<ComboboxSelected>>",lambda e : self.getAllDepartments())

        self.v3 = StringVar()
        self.c2 = Combobox(self.window,textvariable=self.v3,font=myfont1,state='readonly')
        # self.c2.bind("<<ComboboxSelected>>", lambda e: self.getAllCourse())
        self.t1.bind("<FocusIn>", lambda e: self.myfocuscolor("t1", "yellow"))
        self.t1.bind("<FocusOut>", lambda e: self.myfocuscolor("t1", "white"))
        self.t2.bind("<FocusIn>", lambda e: self.myfocuscolor("t2", "yellow"))
        self.t2.bind("<FocusOut>", lambda e: self.myfocuscolor("t2", "white"))
        self.t3.bind("<FocusIn>", lambda e: self.myfocuscolor("t3", "yellow"))
        self.t3.bind("<FocusOut>", lambda e: self.myfocuscolor("t3", "white"))
        self.t6.bind("<FocusIn>", lambda e: self.myfocuscolor("t6", "yellow"))
        self.t6.bind("<FocusOut>", lambda e: self.myfocuscolor("t6", "white"))



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
        self.b7=Button(self.window,text="Clear All Entry Field",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.clearPage)


        self.b6 = Button(self.window,text="Upload",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.selectImage)

        self.imglbl = Label(self.window,relief='groove',borderwidth=2)

        # ------------------- table ------------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8'],height=15)

        self.mytable.heading('c1',text="Roll no")
        self.mytable.heading('c2',text="Name")
        self.mytable.heading('c3',text="Phone")
        self.mytable.heading('c4',text="Gender")
        self.mytable.heading('c5',text="DOB")
        self.mytable.heading('c6',text="Address")
        self.mytable.heading('c7',text="Department")
        self.mytable.heading('c8',text="Course")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=80,anchor='center')
        self.mytable.column('c2',width=80,anchor='center')
        self.mytable.column('c3',width=80,anchor='center')
        self.mytable.column('c4',width=80,anchor='center')
        self.mytable.column('c5',width=80,anchor='center')
        self.mytable.column('c6',width=80,anchor='center')
        self.mytable.column('c7',width=80,anchor='center')
        self.mytable.column('c8',width=80,anchor='center')

        self.mytable.bind("<ButtonRelease>",lambda e : self.getTableData())

        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff*3,y=y1,width=120,height=30)
        self.mytable.place(x=x1+x_diff*3+190,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff*3,y=y1,width=120,height=30)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L4.place(x=x1,y=y1)
        self.r1.place(x=x1+x_diff,y=y1)
        self.r2.place(x=x1+x_diff+x_diff,y=y1)
        y1+=y_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        y1+=y_diff
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L8.place(x=x1,y=y1)
        self.c2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=120,height=40)
        self.b2.place(x=x1+x_diff,y=y1,width=120,height=40)
        self.b3.place(x=x1+x_diff+x_diff,y=y1,width=120,height=40)
        y1 += y_diff
        self.b7.place(x=x1,y=y1,width=230,height=40)
        img_size = 150

        self.imglbl.place(x=x1+400,y=y1-img_size-img_size,width=img_size,height=img_size)
        self.b6.place(x=x1+400,y=y1-img_size,width=img_size,height=40)
        y1 += y_diff

        self.makedatabaseConnection()
        self.getAllDepartments()
        self.getAllCourse()
        self.clearPage()
        self.window.mainloop()

    def myfocuscolor(self, name, color_name):
        if name == "t1":
            self.t1.config(background=color_name)
        elif name == "t2":
            self.t2.config(background=color_name)
        elif name == "t3":
            self.t3.config(background=color_name)
        else:
            self.t6.config(background=color_name)

    def selectImage(self):
        filename = askopenfilename(file= [("All pictures","*.png;*.jpg;*.jpeg"),
                                          ("JPEG Images","*.jpeg"), ("JPG Images","*.jpg"),("PNG Images","*.png")],parent=self.window)
        print("filename = ",filename)
        if filename!="":
            # -------- add image on label ------------------
            self.img1 = Image.open(filename).resize((150,150))
            self.photoimg1 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.photoimg1)

            # -------- make unique name for image ------------
            path = filename.split("/")
            name = path[-1]
            import time
            uniqness = str(int(time.time()))
            self.actualname = uniqness+name

    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e),parent=self.window)
    def saveData(self):
        if self.validate_check()==False:
            return

        if self.actualname == self.default_img_name:
            pass
        else:
            self.img1.save("student_images//"+self.actualname)



        try:

            qry = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),self.t5.get_date(),self.t6.get('0.0',END).strip(),
                    self.v2.get(),self.v3.get(),self.actualname))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Student Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def updateData(self):
        if self.validate_check()==False:
            return
        if self.actualname==self.oldname:
            pass
        else:
            self.img1.save("student_images//"+self.actualname)
            if self.oldname==self.default_img_name:
                pass
            else:
                import os
                os.remove("student_images//"+self.oldname)

        try:

            qry = "update student set name=%s, phone=%s, gender=%s, dob=%s, address=%s, department=%s, course=%s,pic=%s where rollno=%s"

            rowcount = self.curr.execute(qry , (self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get_date(),self.t6.get('0.0',END).strip(),
                    self.v2.get(),self.v3.get(),self.actualname, self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Student Record Updated Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Updation \n"+str(e),parent=self.window)
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ?? ",parent=self.window)
        if ans=="yes":

            if self.oldname==self.default_img_name:
                pass
            else:
                import os
                os.remove("student_images//"+self.oldname)


            try:

                qry = "delete from student where rollno=%s"
                rowcount = self.curr.execute(qry , (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","Student Record Deleted Successfully",parent=self.window)
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
            rollno = self.t1.get()
        else:
            rollno=pk_col
        try:
            qry = "select * from student where rollno=%s"
            rowcount = self.curr.execute(qry , (rollno))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v1.set(data[3])
                self.t5.set_date(data[4])
                self.t6.insert('0.0',data[5])
                self.v2.set(data[6])
                self.v3.set(data[7])
                self.actualname = data[8]
                self.oldname = data[8]
                self.img1 = Image.open("student_images//"+self.actualname).resize((150,150))
                self.photoimg1 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.photoimg1)

                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'

            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v1.set(None)
        self.t5.delete(0,END)
        self.t6.delete('0.0',END)
        self.c1.set("Choose Department")
        self.c2.set("No Course")
        self.getAllData()

        self.actualname=self.default_img_name
        self.img1 = Image.open("student_images//"+self.default_img_name).resize((150,150))
        self.photoimg1 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.photoimg1)

        self.b2['state']='disable'
        self.b3['state']='disable'
    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())

            qry = "select * from student where name like %s "
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
        if not (self.t1.get().isdigit()):
            messagebox.showwarning("Validation Check", "Invalid Roll no", parent=self.window)
            return False
        elif len(self.t2.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter proper name  ", parent=self.window)
            return False
        elif not (self.t3.get().isdigit()) or len(self.t3.get()) != 10:
            messagebox.showwarning("Validation Check", "Enter valid phone no \n10 digits only", parent=self.window)
            return False
        elif not (self.v1.get() == 'Male' or self.v1.get() == 'Female'):
            messagebox.showwarning("Input Error", "Please Select gender ", parent=self.window)
            return False
        elif (self.t5.get() == ""):
            messagebox.showwarning("Input Error", "Please Select DOB ", parent=self.window)
            return False
        elif len(self.t6.get('1.0', END)) < 3:
            messagebox.showwarning("Input Error", "Please Enter Address ", parent=self.window)
            return False
        elif (self.v2.get() == "Choose Department") or (self.v2.get() == "No Department"):
            messagebox.showwarning("Input Error", "Please Select Department ", parent=self.window)
            return False
        elif (self.v3.get() == "Choose Course") or (self.v3.get() == "No Course"):
            messagebox.showwarning("Input Error", "Please Select Course ", parent=self.window)
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


    def getAllCourse(self):
        try:
            qry = "select * from course "
            rowcount = self.curr.execute(qry )
            data = self.curr.fetchall()
            self.courseList=[]
            if data:
                self.c2.set("Choose Course")
                for myrow in data:
                    self.courseList.append(myrow[0])
            else:
                self.c2.set("No Course")

            self.c2.config(values = self.courseList)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyhomepage=Tk()
    StudentClass(dummyhomepage)
    dummyhomepage.mainloop()
