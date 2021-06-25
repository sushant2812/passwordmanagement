import tkinter as tk                
from tkinter import font  as tkfont
from retrival import pg,ret,make
import mysql.connector
from password_generator import generator
from mysql.connector import errorcode
make()
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, DatabasePage,SearchPage,AddPage,AddPage1,UpdatePage,DeletePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="grey")
        self.controller = controller
        self.controller.title("Password Management")
        self.controller.state('zoomed')
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        space=tk.Label(self,height=4,bg='grey')
        space.pack()
        password1=tk.Label(self,text='Enter your password: ',font=('Times New Roman',20),fg='white',bg='grey')
        password1.pack()
        entry=tk.Entry(self,font=('Times New Roman',20),show="*")
        entry.pack(ipady=7)

        def check():
            global a,b
            b=0
            password=str(entry.get())
            try:
                con=mysql.connector.connect(host="localhost",user="root",passwd=password,database='y')
                con.autocommit = True
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                   b=1
                else:
                   b=0
            if b==0:
                pg(password)
                controller.show_frame("MenuPage")
            else:
                incorrect['text']="Incorrect Password"

                
        button=tk.Button(self,text="Enter",command=check,width=20,height=2)
        button.pack(pady=10)
        incorrect=tk.Label(self,text='',font=('Times New Roman',10),fg='white',bg='grey',anchor='n')
        incorrect.pack(fill='both',expand=True)


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        main_menu=tk.Label(self,text='Main Menu',font=('Times New Roman',25),fg='white',bg='grey')
        main_menu.pack()
        selection=tk.Label(self,text='Please make a selection',font=('Times New Roman',25),fg='white',bg='grey',anchor='w')
        selection.pack(fill='x')
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)
        def DatabaseP():
            controller.show_frame("DatabasePage")
        show_database=tk.Button(button_frame,text="Show Entire Database",command=DatabaseP,height=5,width=50)
        show_database.grid(row=0,column=0,pady=5)
        def SearchP():
            controller.show_frame("SearchPage")
        search_database=tk.Button(button_frame,text="Search Database",command=SearchP,height=5,width=50)
        search_database.grid(row=1,column=0,pady=5)
        def AddP():
            controller.show_frame("AddPage")
        search_database=tk.Button(button_frame,text="Add a user",command=AddP,height=5,width=50)
        search_database.grid(row=2,column=0,pady=5)
        def AddP1():
            controller.show_frame("AddPage1")
        search_database=tk.Button(button_frame,text="Add a user with a computer-generated password",command=AddP1,height=5,width=50)
        search_database.grid(row=3,column=0,pady=5)
        def UpdateP():
            controller.show_frame("UpdatePage")
        search_database=tk.Button(button_frame,text="Update a password",command=UpdateP,height=5,width=50)
        search_database.grid(row=4,column=0,pady=5)
        def DeleteP():
            controller.show_frame("DeletePage")
        search_database=tk.Button(button_frame,text="Delete a user-id pair",command=DeleteP,height=5,width=50)
        search_database.grid(row=5,column=0,pady=5)
            

class DatabasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(self,text="Go back",command=MenuPage,height=5,width=50)
        button.pack(pady=25)
        password=ret()
        con=mysql.connector.connect(host="localhost",user="root",passwd=password,database='y')
        cursor=con.cursor()
        cursor.execute("SELECT * FROM y.password;")
        d=cursor.fetchall()
        b=""
        e=["user-id",'password','platform']
        for i in range(0,len(d)):
            for j in range(3):
                b=b+e[j]+":-"+d[i][j]+"\n"
            b=b+"\n"
            
           
        display_text=tk.Text(self,height=50,width=50,font=('Times New Roman',25),fg='white',bg='grey')
        display_text.pack(expand=True)
        display_text.insert(tk.END,b)



        
class SearchPage(tk.Frame):

    def __init__(self, parent, controller,bg='grey'):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="grey")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        platform_label=tk.Label(button_frame,text="Enter platform",height=5,width=10,bg="grey")
        platform_label.grid(row=2,column=0,pady=5,padx=20)
        user=tk.Entry(button_frame,font=('Times New Roman',20))
        user.grid(row=1,column=1,pady=5,padx=20)
        platform=tk.Entry(button_frame,font=('Times New Roman',20))
        platform.grid(row=2,column=1,pady=5,padx=20)
        def search():
            us=str(user.get())
            plat=str(platform.get())
            password=ret()
            con=mysql.connector.connect(host="localhost",user="root",passwd=password,database='y')
            con.autocommit=True
            cursor=con.cursor()
            cursor.execute("SELECT * FROM password WHERE Platform='{}' AND user='{}'".format(plat,us))
            d=cursor.fetchall()
            b=""
            e=["userid","password","platform"]
            con.close()
            if d==[]:
                b="No such user exists!"
            else:
                for j in range(3):
                    b=b+e[j]+':- '
                    for i in d:
                        b=b+i[j]
                        j=j+1
                    b=b+"\n"
            display=tk.Text(button_frame,height=10,width=30)
            display.grid(row=3,column=1)
            display.insert(tk.END,b)
                    
        user_button=tk.Button(button_frame,text="Click Me",command=search,height=2,width=10)
        user_button.grid(row=4,column=1,pady=5,padx=20)



class AddPage(tk.Frame):

    def __init__(self, parent, controller,bg='grey'):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="grey")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter password",height=5,width=20,bg="grey")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        platform_label=tk.Label(button_frame,text="Enter platform",height=5,width=10,bg="grey")
        platform_label.grid(row=3,column=0,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20))
        password1.grid(row=2,column=1,pady=5,padx=20)
        platform1=tk.Entry(button_frame,font=('Times New Roman',20))
        platform1.grid(row=3,column=1,pady=5,padx=20)
        def add():
            user=str(user1.get())
            password=str(password1.get())
            platform=str(platform1.get())
            if user=="" and password=="" and platform=="":
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=3,column=1)
                display.insert(tk.END,"Please try again")
            else:
                passw=ret()
                con=mysql.connector.connect(host="localhost",user="root",passwd=passw,database='y')
                con.autocommit=True
                cursor=con.cursor()
                cursor.execute("INSERT INTO password VALUES('{}','{}','{}')".format(user,password,platform))
                con.close()
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=3,column=1)
                display.insert(tk.END,"Added User Successfully")            
        user_button=tk.Button(button_frame,text="Add",command=add,height=2,width=10)
        user_button.grid(row=5,column=1,pady=5,padx=20)
        
class AddPage1(tk.Frame):

    def __init__(self, parent, controller,bg='grey'):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)##height=2,width=10
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="grey")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter length of the password",height=5,width=30,bg="grey")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        platform_label=tk.Label(button_frame,text="Enter platform",height=5,width=10,bg="grey")
        platform_label.grid(row=3,column=0,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20))
        password1.grid(row=2,column=1,pady=5,padx=20)
        platform1=tk.Entry(button_frame,font=('Times New Roman',20))
        platform1.grid(row=3,column=1,pady=5,padx=20)
        def add():
            user=str(user1.get())
            password=str(password1.get())
            platform=str(platform1.get())
            if user=="" and platform=="" and password=="":
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=3,column=1)
                display.insert(tk.END,"Please try again")
            else:
                b=int(password)
                password=generator(b)
                passw=ret()
                con=mysql.connector.connect(host="localhost",user="root",passwd=passw,database='y')
                con.autocommit=True
                cursor=con.cursor()
                cursor.execute("INSERT INTO password VALUES('{}','{}','{}')".format(user,password,platform))
                con.close()
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=3,column=1)
                display.insert(tk.END,"Added User Successfully")            
        user_button=tk.Button(button_frame,text="Add",command=add)
        user_button.grid(row=5,column=1,pady=5,padx=20)

        
class UpdatePage(tk.Frame):
    def __init__(self, parent, controller,bg='grey'):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="grey")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        platform_label=tk.Label(button_frame,text="Enter platform",height=5,width=10,bg="grey")
        platform_label.grid(row=3,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter new password",height=5,width=20,bg="grey")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        user=tk.Entry(button_frame,font=('Times New Roman',20))
        user.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20))
        password1.grid(row=2,column=1,pady=5,padx=20)
        platform=tk.Entry(button_frame,font=('Times New Roman',20))
        platform.grid(row=3,column=1,pady=5,padx=20)
        
        def update():
            us=str(user.get())
            password=str(password1.get())
            plat=str(platform.get())
            if us=="" and plat=="" and password=="":
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=4,column=1)
                display.insert(tk.END,"Please try again")
            else:
                passw=ret()
                con=mysql.connector.connect(host="localhost",user="root",passwd=passw,database='y')
                con.autocommit=True
                cursor=con.cursor()
                cursor.execute("UPDATE password SET pass='{}' WHERE user='{}' AND Platform='{}';".format(password,us,plat))
                con.close()
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=4,column=1)
                display.insert(tk.END,"Updated Successfully")
        user_button=tk.Button(button_frame,text="Update",command=update)
        user_button.grid(row=4,column=1,pady=5,padx=20)


class DeletePage(tk.Frame):
    def __init__(self, parent, controller,bg='grey'):
        tk.Frame.__init__(self, parent,bg='grey')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Password Database",font=('Times New Roman',45),fg='white',bg='grey')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='grey')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="grey")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        platform_label=tk.Label(button_frame,text="Enter platform",height=5,width=10,bg="grey")
        platform_label.grid(row=3,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter password",height=5,width=20,bg="grey")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        
        user=tk.Entry(button_frame,font=('Times New Roman',20))
        user.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20))
        password1.grid(row=2,column=1,pady=5,padx=20)
        platform=tk.Entry(button_frame,font=('Times New Roman',20))
        platform.grid(row=3,column=1,pady=5,padx=20)
        def delete():
            us=str(user.get())
            password=str(password1.get())
            plat=str(platform.get())
            if us=="" and plat=="" and password=="":
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=4,column=1)
                display.insert(tk.END,"Please try again")
            else:
                passw=ret()
                con=mysql.connector.connect(host="localhost",user="root",passwd=passw,database='y')
                con.autocommit=True
                cursor=con.cursor()
                cursor.execute("DELETE FROM password WHERE user='{}'AND pass='{}' AND platform='{}';".format(us,password,plat))
                con.close()
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=4,column=1)
                display.insert(tk.END,"Deleted Successfully")
        user_button=tk.Button(button_frame,text="Delete",command=delete)
        user_button.grid(row=4,column=1,pady=5,padx=20)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
