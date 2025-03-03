from tkinter import *
from tkinter import ttk, messagebox, filedialog
import pymysql
import os
import credentials as cr
import random
import string
from PIL import Image, ImageTk

class CandidateSignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Candidate Sign Up")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")
        
        self.bg_img = ImageTk.PhotoImage(file="Images/photo1.jpeg")  # Update image path
        background = Label(self.window, image=self.bg_img)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        self.f=Frame(self.window,bg="green2")
        self.f.place(x=8,y=8,width=120,height=50)
        self.bck_button = Button(self.f, text="Back", command=self.bck_button, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=10, y=10, width=80)

        self.fi=Frame(self.window,bg="green2")
        self.fi.place(x=130,y=8,width=120,height=50)
        self.log_button = Button(self.fi, text="LogIn", command=self.log_button, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=10, y=10, width=80)

        frame = Frame(self.window, bg="white")
        frame.place(x=350, y=100, width=500, height=600)

        title1 = Label(frame, text="Candidate Sign Up", font=("times new roman", 25, "bold"), bg="white")
        title1.place(x=20, y=10)

        f_name = Label(frame, text="First name", font=("helvetica", 15, "bold"), bg="white")
        f_name.place(x=20, y=100)
        self.fname_txt = Entry(frame, font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        l_name = Label(frame, text="Last name", font=("helvetica", 15, "bold"), bg="white")
        l_name.place(x=240, y=100)
        self.lname_txt = Entry(frame, font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica", 15, "bold"), bg="white")
        email.place(x=20, y=180)
        self.email_txt = Entry(frame, font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica", 15, "bold"), bg="white")
        sec_question.place(x=20, y=260)
        self.questions = ttk.Combobox(frame, font=("helvetica", 13), state='readonly', justify=CENTER)
        self.questions['values'] = ("Select", "What's your pet name?", "Your first teacher name", "Your birthplace", "Your favorite movie")
        self.questions.place(x=20, y=290, width=200)
        self.questions.current(0)

        answer = Label(frame, text="Answer", font=("helvetica", 15, "bold"), bg="white")
        answer.place(x=240, y=260)
        self.answer_txt = Entry(frame, font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        document_label = Label(frame, text="Upload Document", font=("helvetica", 15, "bold"), bg="white")
        document_label.place(x=20, y=340)
        self.document_btn = Button(frame, text="Choose File", command=self.choose_file, font=("helvetica", 12), bg="light gray")
        self.document_btn.place(x=20, y=370)
        self.document_path = ""

        aadhar_label = Label(frame, text="Aadhar Number", font=("helvetica", 15, "bold"), bg="white")
        aadhar_label.place(x=20, y=420)
        self.aadhar_txt = Entry(frame, font=("arial"))
        self.aadhar_txt.place(x=20, y=450, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.terms, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        terms_and_con.place(x=20, y=480)

        self.signup = Button(frame, text="Sign Up", command=self.signup_func, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white")
        self.signup.place(x=120, y=530, width=250)

    def generate_user_id(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        return password

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", ".pdf"), ("All files", ".*")])
        if file_path:
            self.document_path = file_path
            messagebox.showinfo("File Selected", f"Selected file: {os.path.basename(file_path)}")

    def signup_func(self):
        if self.fname_txt.get() == "" or self.lname_txt.get() == "" or self.email_txt.get() == "" or self.questions.get() == "Select" or self.answer_txt.get() == "" or self.aadhar_txt.get() == "" or self.document_path == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        elif self.terms.get() == 0:
            messagebox.showerror("Error!", "Please Agree with our Terms & Conditions", parent=self.window)
        else:
            try:
                # Connect to MySQL database
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()

                # Check if email already exists
                cur.execute("select * from candidate_regist where email=%s", self.email_txt.get())
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error!", "The email ID already exists, please try again with another email ID", parent=self.window)
                else:
                    # Generate user ID and password
                    user_id = self.generate_user_id()
                    password = self.generate_password()

                    # Insert data into the database
                    cur.execute("insert into candidate_regist(user_id, f_name, l_name, email, question, answer, document_path, aadhar_no, password) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    user_id,
                                    self.fname_txt.get(),
                                    self.lname_txt.get(),
                                    self.email_txt.get(),
                                    self.questions.get(),
                                    self.answer_txt.get(),
                                    self.document_path,
                                    self.aadhar_txt.get(),
                                    password
                                ))

                    # Commit changes and close connection
                    connection.commit()
                    connection.close()

                    messagebox.showinfo("Congratulations!", f"Registration Successful. Your User ID is: {user_id} and Password is: {password}", parent=self.window)
                    self.reset_fields()

            except Exception as es:
                messagebox.showerror("Error!", f"Error due to {es}", parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.aadhar_txt.delete(0, END)
        self.document_path = ""
        self.terms.set(0)

    def bck_button(self):
        self.window.destroy()
        import mai
        root = Tk()
        obj = mai.MainApp(root)
        root.mainloop()

    def bck_button(self):
        self.window.destroy()
        import mai
        root = Tk()
        obj = mai.MainApp(root)
        root.mainloop()
    def log_button(self):
        self.window.destroy()
        import  CandidateLogin
        root = Tk()
        obj = CandidateLogin.CandidateLogin(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = CandidateSignUp(root)
    root.mainloop()