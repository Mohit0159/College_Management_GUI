from tkinter import *
from tkinter import messagebox

from tkinter.ttk import Combobox, Treeview
import pymysql

class FeesClass:
    # default_img_name = "defaultimage.jpg"
    def __init__(self,hwindow):
        # self.window = Tk()  # to create independent window
        self.window = Toplevel(hwindow) # to create child window (studentpage) of hwindow(homepage)
        self.window.title('Fee detail page ')

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

        self.bkimg1 = Image.open("myimages//course_bg.jpg").resize((w1,h1))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window,image=self.bkphotoimg1)
        self.bklbl.place(x=0,y=0)


        # -------------- Widgets --------------------------------------------
        myfont1 = ("Times New Roman",18)
        mycolor1 = "#FFF2F2"
        mycolor2 ="black"
        mycolor3 ="#E33432"
        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window,text="FEE DETAILS ",font=("Georgia",35,"bold"),
                             background=mycolor3,foreground=mycolor1,relief="groove",borderwidth=10)
        self.L1 = Label(self.window,text="Roll no ",font=myfont1,background=mycolor1,foreground=mycolor2,width=12)
        self.L2 = Label(self.window,text="Name ",font=myfont1,background=mycolor1,foreground=mycolor2,width=13)

        self.L4 = Label(self.window, text="Total Fees", font=myfont1, background=mycolor1, foreground=mycolor2, width=13)
        self.L5 = Label(self.window, text="Paid Fees", font=myfont1, background=mycolor1, foreground=mycolor2,
                        width=13)
        self.L6 = Label(self.window, text="Remaining fees", font=myfont1, background=mycolor1, foreground=mycolor2,
                        width=13)
        self.L7 = Label(self.window, text="Paying", font=myfont1, background=mycolor1, foreground=mycolor2,
                        width=13)


        self.v1 = StringVar()
        self.c1 = Combobox(self.window, textvariable=self.v1, font=myfont1, state='readonly')
        self.namebox = Entry(self.window, font=myfont1)

         # self.t2.insert(0, total_fee)
        # self.t3.insert(0, str(paid_fee))
        # self.t4.insert(0, remaing_fee)

        self.t2 = Entry(self.window, font=myfont1)
        self.t3 = Entry(self.window, font=myfont1)
        self.t4 = Entry(self.window, font=myfont1)
        self.t5 = Entry(self.window, font=myfont1)



        self.t2.bind("<FocusIn>", lambda e: self.myfocuscolor("t2", "yellow"))
        self.t2.bind("<FocusOut>", lambda e: self.myfocuscolor("t2", "white"))
        self.t3.bind("<FocusIn>", lambda e: self.myfocuscolor("t3", "yellow"))
        self.t3.bind("<FocusOut>", lambda e: self.myfocuscolor("t3", "white"))
        self.t4.bind("<FocusIn>", lambda e: self.myfocuscolor("t4", "yellow"))
        self.t4.bind("<FocusOut>", lambda e: self.myfocuscolor("t4", "white"))
        self.t5.bind("<FocusIn>", lambda e: self.myfocuscolor("t5", "yellow"))
        self.t5.bind("<FocusOut>", lambda e: self.myfocuscolor("t5", "white"))

        #buttons

        self.b1 = Button(self.window, text="Save", font=myfont1,
                         background=mycolor3, foreground=mycolor1,command=self.saveData)

        # self.b3 = Button(self.window, text="Delete", font=myfont1,
        #                  background=mycolor3, foreground=mycolor1,command=self.deleteData)
        self.b4 = Button(self.window, text="Fetch", font=myfont1,
                         background=mycolor3, foreground=mycolor1,command=self.fetchData)

        self.b6 = Button(self.window, text="Clear All Entry Field", font=myfont1,
                         background=mycolor3, foreground=mycolor1,command=self.clearPage)

        #table---------------------
        self.mytable = Treeview(self.window,columns=['c1', 'c2', 'c3'], height=15)

        self.mytable.heading('c1', text="Roll no")
        self.mytable.heading('c2', text="Name")

        self.mytable.heading('c3', text="Paid Fee")



        self.mytable['show'] = 'headings'

        self.mytable.column('c1', width=150, anchor='center')
        self.mytable.column('c2', width=150, anchor='center')
        self.mytable.column('c3', width=150, anchor='center')



        self.mytable.bind("<ButtonRelease>", lambda e: self.getTableData())


        #placement

        x1 = 50
        y1 = 100
        x_diff = 185
        y_diff = 50
        self.headlbl.place(x=0, y=0, width=w1, height=70)
        self.L1.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        self.b4.place(x=x1 + x_diff*2+84, y=y1, width=120, height=30)
        self.mytable.place(x=x1 + x_diff * 3 + 150, y=y1)
        y1 += y_diff
        self.L2.place(x=x1, y=y1)
        self.namebox.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.L4.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.L5.place(x=x1, y=y1)
        self.t3.place(x=x1+x_diff,y=y1)
        y1 += y_diff
        self.L6.place(x=x1, y=y1)
        self.t4.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.L7.place(x=x1, y=y1)
        self.t5.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.b1.place(x=x1, y=y1, width=120, height=40)

        self.b6.place(x=x1+x_diff, y=y1, width=230, height=40)
        # y1 += y_diff
        # self.b3.place(x=x1, y=y1, width=120, height=40)

        self.makedatabaseConnection()
        # self.getAllname()
        self.getAllrollno()
        self.clearPage()
        # self.getAllData()
        self.window.mainloop()

    def myfocuscolor(self, name, color_name):
        if name == "t2":
            self.t2.config(background=color_name)
        elif name == "t3":
            self.t3.config(background=color_name)
        elif name == "t4":
            self.t4.config(background=color_name)
        else:
            self.t5.config(background=color_name)


    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e),parent=self.window)
    def saveData(self):
        if self.validate_check()==False:
            return
        # self.t2['state'] = 'readonly'
        # self.t3['state'] = 'readonly'
        # self.t4['state'] = 'readonly'
        #
        #

        try:

            qry = "insert into fee_detail values(%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.v1.get(),self.namebox.get(),self.t5.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Fee Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)





    def getTableData(self):
        rowid = self.mytable.focus()
        tabledata = self.mytable.item(rowid)
        selectedRowdata = tabledata['values']
        col0 = selectedRowdata[0]
        self.fetchData(col0)
    def fetchData(self,pk_col=None):
        #nothing to do when use click on table

        try:

            # -- get student record ----

            qry = "select * from student where rollno=%s"
            rowcount = self.curr.execute(qry , (self.v1.get()))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.v1.set(data[0])
                self.namebox.insert(0,data[1])
                self.selectedcourse = data[7]

                #----------- get course fee --------------
                self.curr.execute("select * from course where course_name = %s",(self.selectedcourse))
                cdata = self.curr.fetchone()
                self.selected_course_fee = cdata[4]
                print("selected course name = ",self.selectedcourse)
                print("selected course fee  = ",self.selected_course_fee)

                #------------------------------------------
                self.getfeeDetail()
                # self.t2['state']='readonly'
                # self.t3['state'] = 'readonly'
                # self.t4['state'] = 'readonly'


                if self.t2.get()==self.t3.get():
                    self.b1['state'] = 'disable'
                    messagebox.showinfo("Clear Dues", "All Balance is clear", parent=self.window)
                else:
                    self.b1['state'] = 'normal'
            else:
                messagebox.showinfo("Empty","No Student of this roll no Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion \n" + str(e), parent=self.window)


    def getfeeDetail(self):

        try:
            qry = "select * from fee_detail where rollno=%s"
            rowcount = self.curr.execute(qry , (self.v1.get()))
            data = self.curr.fetchall()
            # self.clearPage()
            #	rollno	name	payment_date	paid_fees

            if data:

                sum=0
                for myrow in data:
                    self.mytable.insert("",END,values=myrow)
                    sum+=myrow[2]
                total_fee=self.selected_course_fee
                paid_fee = sum
                remaing_fee = total_fee-paid_fee

                self.t2.insert(0,total_fee)
                self.t3.insert(0,str(paid_fee))
                self.t4.insert(0, remaing_fee)
            else:
                total_fee=self.selected_course_fee
                self.t2.insert(0,total_fee)
                self.t3.insert(0,'0')
                self.t4.insert(0, total_fee)
                messagebox.showinfo("Empty","No Amount is paid till now",parent=self.window)


        except Exception as e:
            messagebox.showerror("Query Error","Error while Insertion \n"+str(e),parent=self.window)




    def clearPage(self):
        self.c1.set("Choose rollno")
        self.namebox.delete(0,END)
        # self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.mytable.delete(*self.mytable.get_children())

    def validate_check(self):

        if not (self.v1.get().isdigit()):
            messagebox.showwarning("Validation Check", "Invalid Roll no", parent=self.window)
            return False
        elif len(self.namebox.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter proper name  ", parent=self.window)
            return False

        return True



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
    dummyhomepage = Tk()
    FeesClass(dummyhomepage)
    dummyhomepage.mainloop()