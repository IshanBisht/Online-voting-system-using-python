from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import os
from signup_page import SignUp
from login_page import login_page 
import credentials as cr

def show_message(title, message):
    messagebox.showinfo(title, message)

class MainApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Voting Website")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.window.config(bg="white")

        # Adding menubar within header frame
        self.create_header()

        menubar = Menu(self.header_frame)
        self.window.config(menu=menubar)

        # Home menu
        home_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Home", menu=home_menu)

        # Login menu
        login_menu = Menu(menubar, tearoff=0)
        login_menu.add_command(label="Admin Login", command=self.ad_login)
        login_menu.add_command(label="Candidate Login", command=self.can_login)
        login_menu.add_command(label="Voter Login", command=self.voter_login)
        menubar.add_cascade(label="Login", menu=login_menu)

        # Registration menu
        registration_menu = Menu(menubar, tearoff=0)
        registration_menu.add_command(label="Candidate Registration", command=self.candidate_registration)
        registration_menu.add_command(label="Voter Registration", command=self.voter_registration)
        menubar.add_cascade(label="Registration", menu=registration_menu)

        # About menu
        about_menu = Menu(menubar, tearoff=0)
        about_menu.add_command(label="About Us", command=lambda: show_message("About Us", "This is an election management system."))
        menubar.add_cascade(label="About", menu=about_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", command=lambda: show_message("Help", "For assistance, contact support@electionsystem.com."))
        menubar.add_cascade(label="Help", menu=help_menu)

        # Load and resize background image
        self.load_background_image()

        # Add footer
        self.add_footer()

    def load_background_image(self):
        self.window.update_idletasks()  # Ensure window is updated to get the actual size
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        # Load the image
        bg_img = Image.open("Images/OIP.jpeg")
        bg_img = bg_img.resize((window_width, window_height))
        self.bg_img = ImageTk.PhotoImage(bg_img)

        # Set the resized image as the background
        self.background = Label(self.window, image=self.bg_img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

    def create_header(self):
        self.header_frame = Frame(self.window, bg="blue", height=50)
        self.header_frame.pack(fill=X)

        header_label = Label(self.header_frame, text="Election Management System", font=("Arial", 20, "bold"), bg="blue", fg="white")
        header_label.pack(pady=10)

    def add_footer(self):
        footer_frame = Frame(self.window, bg="white", height=30)
        footer_frame.pack(side=BOTTOM, fill=X)

        footer_label = Label(footer_frame, text="© 2024 Election Management System", font=("Arial", 12), bg="white", fg="black")
        footer_label.pack(pady=5)

    
 

    def ad_login(self):
        self.window.destroy()
        import Adminlogin
        root = Tk()
        obj = Adminlogin.AdminLogin(root)
        root.mainloop()
    def can_login(self):
        self.window.destroy()
        import CandidateLogin
        root = Tk()
        obj = CandidateLogin.CandidateLogin(root)
        root.mainloop()
    def voter_login(self):
        self.window.destroy()
        import  login_page
        root = Tk()
        obj = login_page.login_page(root)
        root.mainloop()
    def candidate_registration(self):
        self.window.destroy()
        import CandidateSignUp
        root = Tk()
        obj = CandidateSignUp.CandidateSignUp(root)
        root.mainloop()
    def voter_registration(self):
        self.window.destroy()
        import signup_page
        root = Tk()
        obj = signup_page.SignUp(root)
        root.mainloop()

    

if __name__ == "__main__":
    root = Tk()
    obj = MainApp(root)
    root.mainloop()