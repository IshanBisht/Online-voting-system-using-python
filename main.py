from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from signup_page import SignUp
from login_page import login_page
import credentials as cr

class MainApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Voting Website")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.window.configure(bg="#f5f5f5")

        self.setup_styles()

        self.create_header()
        self.load_background_image()

        self.create_buttons()
        self.add_footer()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 14), padding=10)
        style.configure("Header.TLabel", font=("Segoe UI", 24, "bold"), background="#007acc", foreground="white")
        style.configure("Footer.TLabel", font=("Segoe UI", 10), background="white", foreground="black")

    def create_header(self):
        self.header_frame = Frame(self.window, bg="#007acc", height=60)
        self.header_frame.pack(fill=X, side=TOP)

        header_label = ttk.Label(self.header_frame, text="Election Management System", style="Header.TLabel")
        header_label.pack(pady=10)

    def load_background_image(self):
        self.window.update_idletasks()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        try:
            bg_img = Image.open("Images/OIP.jpeg")
            bg_img = bg_img.resize((window_width, window_height))
            self.bg_img = ImageTk.PhotoImage(bg_img)
            self.background = Label(self.window, image=self.bg_img)
            self.background.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Background image not found.")

    def create_buttons(self):
        # Button frame
        btn_frame = Frame(self.window, bg="#ffffff", padx=30, pady=30)
        btn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Login Section
        login_label = Label(btn_frame, text="Login", font=("Segoe UI", 16, "bold"), bg="white")
        login_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Button(btn_frame, text="Admin Login", command=self.ad_login).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="Candidate Login", command=self.can_login).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(btn_frame, text="Voter Login", command=self.voter_login).grid(row=2, column=0, columnspan=2, pady=10)

        # Signup Section
        signup_label = Label(btn_frame, text="Registration", font=("Segoe UI", 16, "bold"), bg="white")
        signup_label.grid(row=3, column=0, columnspan=2, pady=(30, 10))

        ttk.Button(btn_frame, text="Candidate Registration", command=self.candidate_registration).grid(row=4, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="Voter Registration", command=self.voter_registration).grid(row=4, column=1, padx=10, pady=10)

    def add_footer(self):
        footer_frame = Frame(self.window, bg="white", height=30)
        footer_frame.pack(side=BOTTOM, fill=X)

        footer_label = ttk.Label(footer_frame, text="© 2024 Election Management System", style="Footer.TLabel")
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
        import login_page
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
