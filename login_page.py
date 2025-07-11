from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import credentials as cr

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Voter Login")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450,relheight=1)

        self.bck_button = Button(self.frame1, text="Back", command=self.bck_button, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=20, y=20, width=120)
        

        Label(self.frame1, text="Election", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=0, y=300)
        label2 = Label(self.frame1, text="Campaign", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=185, y=300)
        label3 = Label(self.frame1, text="It's all about the right choices and futures", font=("times new roman", 13, "bold"), bg="yellow", fg="brown4").place(x=100, y=360)

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        self.id_label = Label(self.frame3, text="User ID", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=40)
        self.id_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.id_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3, text="Password", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=140)
        self.password_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show='*')
        self.password_entry.place(x=50, y=180, width=300)

        self.login_button = Button(self.frame3, text="Log In", command=self.login_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="blue", fg="white").place(x=50, y=240, width=300)

        self.forgotten_pass = Button(self.frame3, text="Forgotten password?", command=self.forgot_func, font=("times new roman", 10, "bold"), bd=0, cursor="hand2", bg="white", fg="blue").place(x=125, y=300, width=150)

        self.create_button = Button(self.frame3, text="Create New Account", command=self.redirect_window, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=80, y=360, width=250)

    def login_func(self):
        if self.id_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from voter_regist where user_id=%s and password=%s", (self.id_entry.get(), self.password_entry.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error!", "Invalid User ID or Password", parent=self.window)
                else:
                    messagebox.showinfo("Success", "Login Successful", parent=self.window)
                    self.open_dashboard(self.id_entry.get()) 
                connection.close()
            except Exception as es:
                messagebox.showerror("Error!", f"Error due to {es}", parent=self.window)

    def open_dashboard(self, user_id):
        self.window.destroy()
        import  UserDashboard
        root = Tk()
        obj =UserDashboard.UserDashboard(root, user_id)  # Pass the user_id to CandidateDashboard
        root.mainloop()
    
    def forgot_func(self):
        # Implementation for forgotten password can be added here
        messagebox.showinfo("Info", "Forgotten password functionality is not implemented yet", parent=self.window)

    def redirect_window(self):
        self.window.destroy()
        import signup_page
        root = Tk()
        obj = signup_page.SignUp(root)
        root.mainloop()

    def bck_button(self):
        self.window.destroy()
        import mai
        root = Tk()
        obj = mai.MainApp(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()