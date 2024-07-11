from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

import pymysql


class UserClass:
    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
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

        self.bkimg1 = Image.open("myimages//Up_bg.jpg").resize((w1, h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window, image=self.bkphotoimg1)
        self.bklbl.place(x=0, y=0)

        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="User",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Username",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L2 = Label(self.window,text="Password",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L3 = Label(self.window,text="Usertype",font=myfont1,background=mycolor1,foreground=mycolor2)


        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,values=['Admin','Employee'] ,textvariable=self.v1,
                           font=myfont1,state='readonly')



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
        self.b6 = Button(self.window, text="Clear Entry Field", font=myfont1,
                         background=mycolor3, foreground=mycolor1, command=self.clearPage)

        # ------------------- table ------------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2'],height=10)

        self.mytable.heading('c1',text="Username")
        self.mytable.heading('c2',text="Usertype")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=200,anchor='center')
        self.mytable.column('c2',width=200,anchor='center')

        self.mytable.bind("<ButtonRelease>",lambda e : self.getTableData())

        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff*3+20,y=y1,width=120,height=30)
        self.mytable.place(x=x1+x_diff*3+200,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff*3+20,y=y1,width=120,height=30)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=120,height=40)
        self.b2.place(x=x1+x_diff,y=y1,width=120,height=40)
        self.b3.place(x=x1+x_diff+x_diff,y=y1,width=120,height=40)
        y1 += y_diff
        self.b6.place(x=x1, y=y1, width=350, height=40)

        self.makedatabaseConnection()
        self.clearPage()
        self.window.mainloop()

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
            qry = "insert into usertable values(%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get(),self.v1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def updateData(self):
        if self.validate_check()==False:
            return
        try:

            qry = "update usertable set password=%s, usertype=%s where username=%s"

            rowcount = self.curr.execute(qry , (self.t2.get(),self.v1.get(), self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Updated Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Updation \n"+str(e),parent=self.window)
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ?? ",parent=self.window)
        if ans=="yes":
            try:
                qry = "delete from usertable where username=%s"
                rowcount = self.curr.execute(qry , (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","User Record Deleted Successfully",parent=self.window)
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
            uname = self.t1.get()
        else:
            uname=pk_col
        try:
            qry = "select * from usertable where username=%s"
            rowcount = self.curr.execute(qry , (uname))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])

            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.c1.set("Choose Usertype")
        self.getAllData()

    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())
            utype = self.v1.get()
            if utype=="Choose Usertype":
                utype=""

            qry = "select * from usertable where usertype like %s "
            rowcount = self.curr.execute(qry ,(utype+"%"))
            data = self.curr.fetchall()
            if data:
                for myrow in data:
                    r1 = [myrow[0],myrow[2]]
                    self.mytable.insert('',END,values=r1)
            else:
                messagebox.showinfo("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)
    def validate_check(self):
        if len(self.t1.get())<1:
            messagebox.showwarning("Validation Check", "Enter username", parent=self.window)
            return False
        elif len(self.t2.get()) < 1:
            messagebox.showwarning("Validation Check", "Enter Password  ", parent=self.window)
            return False
        elif (self.v1.get() == "Choose Usertype"):
            messagebox.showwarning("Input Error", "Please Select Usertype ", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummyhomepage=Tk()
    UserClass(dummyhomepage)
    dummyhomepage.mainloop()
