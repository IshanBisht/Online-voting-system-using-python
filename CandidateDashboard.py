from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import mysql.connector

class CandidateDashboard:
    def __init__(self, root, user_id):
        self.window = root
        self.user_id = user_id
        self.window.title("Candidate Dashboard")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")

        Label(self.window, text="Fill the candidate Form", font=("helvetica", 30, "bold"), bg="white", fg="black").grid(row=0, columnspan=2, pady=20)

        # Load user data if available
        self.load_user_data()

        # Create form
        self.create_form()

    def load_user_data(self):
        self.user_data = None
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nik@102004",
            database="student_database"
        )
        cursor = conn.cursor()
        cursor.execute('SELECT photo_path, party_name, election_name, achievements, candidate_name FROM can_dashboard WHERE user_id=%s', (self.user_id,))
        self.user_data = cursor.fetchone()
        conn.close()

    def create_form(self):
        # Candidate's Picture
        self.photo_label = Label(self.window, text="Upload Picture:", font=("helvetica", 14), bg="white")
        self.photo_label.grid(row=1, column=0, pady=10, sticky=W)

        self.upload_btn = Button(self.window, text="Choose File", command=self.upload_photo, bd=0, cursor="hand2", bg="green2", fg="white")
        self.upload_btn.grid(row=1, column=1, pady=10, sticky=W)

        self.photo_canvas = Canvas(self.window, width=150, height=150, bg="white", highlightthickness=0)
        self.photo_canvas.grid(row=2, columnspan=2, pady=10)

        # Party Name
        self.name_label = Label(self.window, text="Party Name:", font=("helvetica", 14), bg="white")
        self.name_label.grid(row=3, column=0, pady=10, sticky=W)

        self.party_entry = Entry(self.window, font=("helvetica", 14), width=50)
        self.party_entry.grid(row=3, column=1, pady=10, sticky=W)

        # Election Name
        self.election_label = Label(self.window, text="Election Name:", font=("helvetica", 14), bg="white")
        self.election_label.grid(row=4, column=0, pady=10, sticky=W)

        self.election_entry = Entry(self.window, font=("helvetica", 14), width=50)
        self.election_entry.grid(row=4, column=1, pady=10, sticky=W)

        # Achievements
        self.achievements_label = Label(self.window, text="Achievements:", font=("helvetica", 14), bg="white")
        self.achievements_label.grid(row=5, column=0, pady=10, sticky=NW)

        self.achievements_text = Text(self.window, font=("helvetica", 14), width=60, height=10)
        self.achievements_text.grid(row=5, column=1, pady=10, sticky=W)

        # Candidate Name
        self.candidate_name_label = Label(self.window, text="Candidate Name:", font=("helvetica", 14), bg="white")
        self.candidate_name_label.grid(row=6, column=0, pady=10, sticky=W)

        self.candidate_entry = Entry(self.window, font=("helvetica", 14), width=50)
        self.candidate_entry.grid(row=6, column=1, pady=10, sticky=W)

        # Pre-fill the form if data exists
        if self.user_data:
            photo_path, party_name, election_name, achievements, candidate_name = self.user_data
            if photo_path:
                self.photo_path = photo_path
                self.display_photo()
            self.party_entry.insert(0, party_name)
            self.election_entry.insert(0, election_name)
            self.achievements_text.insert("1.0", achievements)
            self.candidate_entry.insert(0, candidate_name)

        # Submit Button
        self.submit_btn = Button(self.window, text="Submit", font=("helvetica", 14), command=self.submit_form, bd=0, cursor="hand2", bg="green2", fg="white")
        self.submit_btn.grid(row=7, column=0, pady=20, sticky=W)

        # Review Button
        self.review_btn = Button(self.window, text="Review", font=("helvetica", 14), command=self.review_form, bd=0, cursor="hand2", bg="green2", fg="white")
        self.review_btn.grid(row=7, column=1, pady=20, sticky=W)

        # Logout button
        self.log = Button(self.window, text="Logout", font=("helvetica", 14), command=self.log_button, bd=0, cursor="hand2", bg="green2", fg="white")
        self.log.grid(row=1, column=9, pady=20, sticky=W)

        # Review Form Frame
        self.review_frame = Frame(self.window, bg="white")
        self.review_frame.grid(row=7, columnspan=2, pady=20)

    def upload_photo(self):
        self.photo_path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
        if self.photo_path:
            self.photo_label.config(text=f"Selected File: {self.photo_path.split('/')[-1]}")
            self.display_photo()

    def log_button(self):
        self.window.destroy()
        import CandidateLogin
        root = Tk()
        obj = CandidateLogin.CandidateLogin(root)
        root.mainloop()

    def display_photo(self):
        img = Image.open(self.photo_path).resize((150, 150))
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img.size, fill=255)
        img.putalpha(mask)
        img = ImageTk.PhotoImage(img)
        self.photo_canvas.create_image(75, 75, image=img)
        self.photo_canvas.image = img

    def review_form(self):
        review_window = Toplevel(self.window)
        review_window.title("Review Form")
        review_window.geometry("600x600")
        review_window.config(bg="white")

        if hasattr(self, 'photo_path'):
            img = Image.open(self.photo_path).resize((150, 150))
            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + img.size, fill=255)
            img.putalpha(mask)
            img = ImageTk.PhotoImage(img)
            photo_label = Label(review_window, image=img, bg="white")
            photo_label.image = img
            photo_label.pack(pady=20)
        else:
            Label(review_window, text="Photo: Not Uploaded", font=("helvetica", 14), bg="white").pack(pady=20)

        Label(review_window, text=f"Candidate Name: {self.candidate_entry.get()}", font=("helvetica", 14), bg="white").pack(pady=10)
        Label(review_window, text=f"Party Name: {self.party_entry.get()}", font=("helvetica", 14), bg="white").pack(pady=10)
        Label(review_window, text=f"Election Name: {self.election_entry.get()}", font=("helvetica", 14), bg="white").pack(pady=10)
        Label(review_window, text="Achievements:", font=("helvetica", 14), bg="white").pack(pady=10)
        achievements_label = Label(review_window, text=self.achievements_text.get("1.0", END), font=("helvetica", 14), bg="white", wraplength=500, justify=LEFT)
        achievements_label.pack(pady=10)

    def submit_form(self):
        candidate_name = self.candidate_entry.get()
        party_name = self.party_entry.get()
        election_name = self.election_entry.get()
        achievements = self.achievements_text.get("1.0", END)

        if hasattr(self, 'photo_path'):
            photo_path = self.photo_path
        else:
            photo_path = None

        # Save details to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nik@102004",
            database="student_database"
        )
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO can_dashboard (user_id, photo_path, party_name, election_name, achievements, candidate_name)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        photo_path=VALUES(photo_path), party_name=VALUES(party_name), election_name=VALUES(election_name), achievements=VALUES(achievements), candidate_name=VALUES(candidate_name)
        ''', (self.user_id, photo_path, party_name, election_name, achievements, candidate_name))

        conn.commit()
        conn.close()

        # Show confirmation message
        Label(self.window, text="Form Submitted Successfully!", font=("helvetica",14),bg="white",fg="green").grid(row=8,columnspan=2,pady=20)
if __name__=="__main__":
    root=Tk()
    obj=CandidateDashboard(root,user_id="dummy_user_id")
    root.mainloop()