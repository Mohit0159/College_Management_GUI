from tkinter import *
from tkinter import messagebox

from ChangePassword import ChangePasswordClass
from CoursePage import CourseClass
from DepartmentPage import DepartmentClass
from Fee_detail import FeesClass
from Studentreportpage1 import StudentReport1
from courseReportpage import CourseReportPage
from coursereportpage2 import CourseReportPage2
from departmentReport import DepartmentReport
from fees_reportpage import FeeReportPage2
from studentreportpage2 import StudentReportPage2
from Reportpage3 import StudentReportPage3
from studentpage import StudentClass
from UserPage import UserClass
from teacherpage import TeacherClass
from teacherreportpage1 import TeacherReportClass


class HomepageClass:
    def __init__(self,uname,utype):
        self.uname = uname
        self.utype = utype
        self.window = Tk()
        self.window.title("CMS")
        self.window.config(background="gray")
        self.window.title('Homepage')
        # ----- setting -------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int( w/2  )
        h1 = int( h/2 )
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1 , int(w1 - w1/2 )  , int(h1-h1/2)))  # (width,height,x,y)
        self.window.state("zoomed")

        #--------------- background -----------------------
        from PIL import Image,ImageTk

        self.bkimg1 = Image.open("myimages//homepage_bg.jpg").resize((w,h))
        self.bkphotoimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.window,image=self.bkphotoimg1)
        self.bklbl.place(x=0,y=0)

        # ------------------------------------------------------



        #-------------- menus -------------------
        self.window.option_add("*TearOff",False)
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)

        self.menu1 = Menu(self.menubar)
        self.menu2 = Menu(self.menubar)
        self.menu3 = Menu(self.menubar)
        self.menu4 = Menu(self.menubar)
        self.menu5 = Menu(self.menubar)


        self.menubar.add_cascade(menu=self.menu1 , label="Information")
        self.menubar.add_cascade(menu=self.menu2 , label="Details")
        self.menubar.add_cascade(menu=self.menu3 , label="Reports")
        self.menubar.add_cascade(menu=self.menu4, label="Fee")
        self.menubar.add_cascade(menu=self.menu5 , label="Account")


        self.iconimg4 = Image.open("myimages//Student_icon.png").resize((20, 20))
        self.iconphotoimg4 = ImageTk.PhotoImage(self.iconimg4)

        self.iconimg5 = Image.open("myimages//Teacher_icon.png").resize((20, 20))
        self.iconphotoimg5 = ImageTk.PhotoImage(self.iconimg5)
        # self.menu1.add_command(label="Student",command=lambda : StudentClass())  # to open independent window

        self.menu1.add_command(label="Student",command=lambda : StudentClass(self.window),accelerator="Ctrl+s",image=self.iconphotoimg4,compound=LEFT) # to open dependent window
        self.window.bind("<Control-s>", lambda e: StudentClass(self.window))
        self.menu1.add_command(label="Teacher",command=lambda :TeacherClass(self.window),accelerator="Ctrl+t",image=self.iconphotoimg5,compound=LEFT)
        self.window.bind("<Control-t>", lambda e: TeacherClass(self.window))
        self.iconimg7 = Image.open("myimages//dept_icon.png").resize((20, 20))
        self.iconphotoimg7 = ImageTk.PhotoImage(self.iconimg7)
        self.menu2.add_command(label="Department",command=lambda : DepartmentClass(self.window),accelerator="Ctrl+d",compound=LEFT,image=self.iconphotoimg7)
        self.window.bind("<Control-d>",lambda e : DepartmentClass(self.window))
        self.iconimg16 = Image.open("myimages//course_icon.png").resize((20, 20))
        self.iconphotoimg16 = ImageTk.PhotoImage(self.iconimg16)
        self.menu2.add_command(label="Course",command=lambda : CourseClass(self.window),accelerator="Ctrl+c",compound=LEFT,image=self.iconphotoimg16)
        self.window.bind("<Control-c>", lambda e: CourseClass(self.window))

        self.iconimg8 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg8 = ImageTk.PhotoImage(self.iconimg8)

        self.menu3.add_command(label="All Student",command=lambda :StudentReport1(self.window),compound=LEFT,image=self.iconphotoimg8)

        self.iconimg9 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg9 = ImageTk.PhotoImage(self.iconimg9)

        self.menu3.add_command(label="Student By Department",command=lambda :StudentReportPage2(self.window),compound=LEFT,image=self.iconphotoimg9)

        self.iconimg10 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg10 = ImageTk.PhotoImage(self.iconimg10)

        self.menu3.add_command(label="Student By DOB",command=lambda :StudentReportPage3(self.window),compound=LEFT,image=self.iconphotoimg10)

        self.iconimg11 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg11 = ImageTk.PhotoImage(self.iconimg11)
        self.menu3.add_command(label="All Teachers", command=lambda:TeacherReportClass(self.window),compound=LEFT,image=self.iconphotoimg11)

        self.iconimg12 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg12 = ImageTk.PhotoImage(self.iconimg12)
        self.menu3.add_command(label="All Departments", command=lambda:DepartmentReport(self.window),compound=LEFT,image=self.iconphotoimg12)

        self.iconimg13 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg13 = ImageTk.PhotoImage(self.iconimg13)
        self.menu3.add_command(label="All Courses", command=lambda:CourseReportPage(self.window),compound=LEFT,image=self.iconphotoimg13)

        self.iconimg14 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg14 = ImageTk.PhotoImage(self.iconimg14)
        self.menu3.add_command(label="All Courses By Department", command=lambda: CourseReportPage2(self.window),compound=LEFT,image=self.iconphotoimg14)

        self.iconimg15 = Image.open("myimages//Report_icon1.png").resize((15, 15))
        self.iconphotoimg15 = ImageTk.PhotoImage(self.iconimg15)
        self.menu3.add_command(label="Fee Detail By Roll No", command=lambda: FeeReportPage2(self.window),compound=LEFT,image=self.iconphotoimg15)

        self.iconimg6 = Image.open("myimages//fees_icon.png").resize((20, 20))
        self.iconphotoimg6 = ImageTk.PhotoImage(self.iconimg6)
        self.menu4.add_command(label="Student Fee", command=lambda: FeesClass(self.window), accelerator="Ctrl+f",compound=LEFT,image=self.iconphotoimg6)
        self.window.bind("<Control-f>", lambda e: FeesClass(self.window))

        self.iconimg1 = Image.open("myimages//use_icon.png").resize((20, 20))
        self.iconphotoimg1 = ImageTk.PhotoImage(self.iconimg1)

        self.iconimg2 = Image.open("myimages//cp_icon.png").resize((20, 20))
        self.iconphotoimg2 = ImageTk.PhotoImage(self.iconimg2)

        self.iconimg3 = Image.open("myimages//logout_icon.png").resize((20, 20))
        self.iconphotoimg3 = ImageTk.PhotoImage(self.iconimg3)

        self.menu5.add_command(label="Manage User",command=lambda : UserClass(self.window),
                               image=self.iconphotoimg1,compound=LEFT)
        self.menu5.add_command(label="Change Password",command=lambda : ChangePasswordClass(self.window,self.uname),
                               image=self.iconphotoimg2,compound=LEFT)
        self.menu5.add_command(label="Logout",command=self.quitter,image=self.iconphotoimg3,compound=LEFT)


        if self.utype == 'Employee':
            self.menubar.delete(0)
            self.menubar.entryconfig(0,state='disable')


            # self.menu3.entryconfig(1,state='disable')
            # self.menu3.entryconfig(2, state='disable')
            # self.menu3.entryconfig(6, state='disable')


            # self.menu3.delete(1)
            # self.menu3.delete(2)
            # self.menu3.delete(6)
            # self.menu3.delete(7)
        #

        self.window.mainloop()
    def quitter(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to Logout ?? ",parent=self.window)
        if ans=="yes":
            self.window.destroy()
            from LoginPage import LoginClass
            LoginClass()