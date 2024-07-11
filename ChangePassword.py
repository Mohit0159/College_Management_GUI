from tkinter import *
from tkinter import messagebox

import pymysql


class ChangePasswordClass:
    def __init__(self,hwindow,un):
        self.uname =un
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

        self.bkimg1 = Image.open("myimages//Cp_bg.jpg").resize((w1, h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window, image=self.bkphotoimg1)
        self.bklbl.place(x=0, y=0)

        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="Change Password",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Current Password",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L2 = Label(self.window,text="New Password",font=myfont1,background=mycolor1,foreground=mycolor2)
        self.L3 = Label(self.window,text="Confirm Password",font=myfont1,background=mycolor1,foreground=mycolor2)


        self.t1 = Entry(self.window,font=myfont1,show='*')
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.t3 = Entry(self.window,font=myfont1,show='*')
        self.b2 = Button(self.window,text="Change Password",font=myfont1,
                         background=mycolor3,foreground=mycolor1,command=self.updateData)




        #-----------------placements --------------------------------------
        x1 = 50
        y1 = 100
        x_diff = 200
        y_diff=50

        self.headlbl.place(x=0,y=0,width=w1,height=70)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b2.place(x=x1+x_diff,y=y1,width=200,height=40)
        y1 += y_diff
        

        self.makedatabaseConnection()
        self.clearPage()
        self.window.mainloop()

    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e),parent=self.window)

    def updateData(self):
        if self.t2.get()!=self.t3.get():
            messagebox.showwarning("Not match","Confirm Password carefully",parent=self.window)
            return

        try:
            qry = "update usertable set password=%s where username=%s and password=%s"
            rowcount = self.curr.execute(qry , (self.t2.get(), self.uname, self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Password Changed Successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showwarning("Failure","Wrong password",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Updation \n"+str(e),parent=self.window)


    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)