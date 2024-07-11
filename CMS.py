from tkinter import messagebox
import pymysql
class MainClass:
    def __init__(self):
        self.makedatabaseConnection()
        try:
            qry = "select * from usertable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            if data:
                from LoginPage import LoginClass
                LoginClass()
            else:
                from createadmin import CreateAdminClass
                CreateAdminClass()
        except Exception as e:
            messagebox.showerror("Query Error", "Error while getting data \n" + str(e))

    def makedatabaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="cms_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting Database \n"+str(e))


if __name__ == '__main__':
    MainClass()