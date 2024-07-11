from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

class CreateAdminClass:
    def __init__(self):
        self.window = Tk()
        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w/2  )
        h1 = int( h/2 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1 , int(w1 - w1/2 )  , int(h1-h1/2)))
        self.window.title('Create admin')



        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Welcome to CMS",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Username",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L2 = Label(self.window,text="Password",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L3 = Label(self.window,text="Usertype",font=myfont1,background=mycolor1,foreground=mycolor2)


        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,values=['Admin','Employee'] ,textvariable=self.v1,
                           font=myfont1,state='disable')
        self.c1.current(0)




        self.b1 = Button(self.window,text="Create Admin",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.saveData)
        self.b2 = Button(self.window, text="Clear Entry Field", font=myfont1,
                         background=mycolor3, foreground=mycolor1, command=self.clearPage)

        #-----------------placements --------------------------------------
        x1 = 200
        y1 = 100
        x_diff = 130
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=410,height=40)
        y1 += y_diff
        self.b2.place(x=x1,y=y1,width=410,height=40)
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
                messagebox.showinfo("Success","Admin Created Successfully",parent=self.window)
                self.window.destroy()
                from LoginPage import LoginClass
                LoginClass()

        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)

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
    CreateAdminClass()