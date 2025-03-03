from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import pymysql
import credentials as cr

def fetch_admin_id():
    return "Admin123"

class AdminDashboard:
    def __init__(self, root):
        self.window = root
        self.window.title("Admin Dashboard")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")

        self.admin_id = fetch_admin_id()
        self.profile_pic = None

        self.menu_frame = Frame(self.window, bg="blue", width=300, height=800)
        self.menu_frame.place(x=0, y=0)

        self.admin_label = Label(self.menu_frame, text=f"Admin ID: {self.admin_id}", font=("helvetica", 16), bg="lightgray")
        self.admin_label.pack(pady=20)

        self.upload_button = Button(self.menu_frame, text="Upload Picture", command=self.upload_picture)
        self.upload_button.pack(pady=20)

        self.candidate_details_button = Button(self.menu_frame, text="Candidate's Details", command=self.show_candidate_details)
        self.candidate_details_button.pack(pady=20)

        self.results_button = Button(self.menu_frame, text="Results", command=self.show_results)
        self.results_button.pack(pady=20)

        self.content_frame = Frame(self.window, bg="white", width=980, height=800)
        self.content_frame.place(x=300, y=0)
        self.welcome_label = Label(self.content_frame, text="Welcome to the Admin Dashboard", font=("helvetica", 30, "bold"), bg="white", fg="black")
        self.welcome_label.pack(pady=50)

    def upload_picture(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.profile_pic = Image.open(file_path)
            self.profile_pic = self.profile_pic.resize((150, 150))
            self.profile_pic = ImageTk.PhotoImage(self.profile_pic)
            self.picture_label.config(image=self.profile_pic)

    def show_candidate_details(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        canvas = Canvas(self.content_frame, width=960, height=800)
        scrollbar = Scrollbar(self.content_frame, orient="vertical", command=canvas.yview, width=20)
        scrollable_frame = Frame(canvas, width=940, height=780)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nik@102004",  
            database="student_database"
        )
        cursor = conn.cursor()
        cursor.execute('SELECT user_id, party_name, election_name, achievements, photo_path FROM can_dashboard')
        candidates = cursor.fetchall()
        conn.close()

        for candidate in candidates:
            user_id, party_name, election_name, achievements, photo_path = candidate

            frame = Frame(scrollable_frame, bg="light blue", bd=1, relief="solid")
            frame.pack(fill="x", padx=10, pady=5)

            if photo_path:
                img = Image.open(photo_path)
                img = img.resize((100, 100))
                photo = ImageTk.PhotoImage(img)
                img_label = Label(frame, image=photo, bg="yellow")
                img_label.image = photo
                img_label.pack(side="left", padx=10)

            details_frame = Frame(frame, bg="light blue")
            details_frame.pack(side="left", fill="x", expand=True)

            Label(details_frame, text=f"User ID: {user_id}", font=("TimesNew Roman", 14), bg="white").pack(anchor="w", pady=2)
            Label(details_frame, text=f"Party Name: {party_name}", font=("Arial", 14), bg="white").pack(anchor="w", pady=2)
            Label(details_frame, text=f"Election Name: {election_name}", font=("helvetica", 14), bg="white").pack(anchor="w", pady=2)
            Label(details_frame, text=f"Achievements: {achievements}", font=("Arial", 14), bg="white", wraplength=600).pack(anchor="w", pady=2)
            delete_button = Button(frame, text="Delete", command=lambda uid=user_id: self.delete_candidate(uid))
            delete_button.pack(anchor="e", pady=2)

    def delete_candidate(self, user_id):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nik@102004",  # Replace with your MySQL password
            database="student_database"
        )
        cursor = conn.cursor()
        cursor.execute('DELETE FROM can_dashboard WHERE user_id=%s', (user_id,))
        conn.commit()
        conn.close()
        self.show_candidate_details()

    def show_results(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.results_button = Button(self.content_frame, text="View Results", command=self.view_results, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.results_button.place(x=20, y=20, width=200, height=40)

        self.results_frame = Frame(self.content_frame, bg="white")
        self.results_frame.place(x=20, y=80, width=940, height=700)

        self.canvas = Canvas(self.results_frame, bg="white")
        self.scrollbar = Scrollbar(self.results_frame,orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def view_results(self):
        # Clear previous results
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cur = connection.cursor()

            # Fetch candidate details and image paths
            cur.execute("SELECT user_id, party_name, photo_path FROM can_dashboard")
            candidates = cur.fetchall()

            # Fetch vote counts
            cur.execute("SELECT party_name, COUNT(*) as votes FROM votes GROUP BY party_name")
            votes = cur.fetchall()
            votes_dict = {party: count for party, count in votes}

            Label(self.scrollable_frame, text="Candidate Details", font=("times new roman", 20, "bold"), bg="white").pack()

            for candidate in candidates:
                candidate_name, party_name, image_path = candidate
                vote_count = votes_dict.get(party_name, 0)
                candidate_info = f"Candidate Name: {candidate_name}\n Party: {party_name}\n Votes: {vote_count}"

                frame = Frame(self.scrollable_frame, bg="light blue", bd=1, relief="solid")
                frame.pack(fill="x", padx=10, pady=5)

                # Display candidate image
                img = Image.open(image_path)
                img = img.resize((100, 100))
                photo = ImageTk.PhotoImage(img)
                img_label = Label(frame, image=photo, bg="white")
                img_label.image = photo
                img_label.pack(side="left", padx=10)

                # Display candidate information
                info_label = Label(frame, text=candidate_info, font=("times new roman", 15), bg="white", anchor="w", justify=LEFT)
                info_label.pack(side="left", fill="x", expand=True)

            connection.close()
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}", parent=self.window)


if __name__ == "__main__":
    root = Tk()
    obj = AdminDashboard(root)
    root.mainloop()