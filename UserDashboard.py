from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import credentials as cr

class UserDashboard:
    def __init__(self, root, user_id):
        self.window = root
        self.window.title("User Dashboard")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")
        self.user_id = user_id  # Assuming user_id is passed when UserDashboard is initialized

        Label(self.window, text="Welcome to the User Dashboard", font=("times new roman", 40, "bold"), bg="white", fg="blue").pack(pady=20)

        self.f = Frame(self.window, bg="green2")
        self.f.place(x=8, y=8, width=120, height=50)
        Button(self.f, text="Logout", command=self.logout, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=10, y=10, width=80)

        self.canvas = Canvas(self.window, bg="white")
        self.scrollbar = ttk.Scrollbar(self.window, orient=VERTICAL, command=self.canvas.yview)
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

        # Load voted candidate data
        self.load_voted_candidate()
        # Load candidate data
        self.load_candidate_data()

    def load_voted_candidate(self):
        conn = mysql.connector.connect(
            host=cr.host,
            user=cr.user,
            password=cr.password,
            database=cr.database
        )
        cursor = conn.cursor()
        cursor.execute('SELECT candidate_id FROM votes WHERE user_id=%s', (self.user_id,))
        self.voted_candidate_id = cursor.fetchone()
        conn.close()

    def load_candidate_data(self):
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        conn = mysql.connector.connect(
            host=cr.host,
            user=cr.user,
            password=cr.password,
            database=cr.database
        )
        cursor = conn.cursor()
        cursor.execute('SELECT id, user_id, photo_path, party_name, election_name, achievements FROM can_dashboard')
        candidates = cursor.fetchall()
        conn.close()

        for candidate in candidates:
            self.create_candidate_form(candidate)

    def create_candidate_form(self, candidate_data):
        candidate_id, user_id, photo_path, party_name, election_name, achievements = candidate_data
        
        frame = Frame(self.scrollable_frame, bg="white", bd=2, relief=SOLID)
        frame.pack(pady=10, padx=10, fill=X)

        if photo_path:
            try:
                img = Image.open(photo_path).resize((100, 100))
                img = ImageTk.PhotoImage(img)
                photo_label = Label(frame, image=img, bg="white")
                photo_label.image = img
                photo_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
            except Exception as e:
                print(f"Error loading image: {e}")
                Label(frame, text="No Image", bg="white").grid(row=0, column=0, rowspan=3, padx=10, pady=10)
        else:
            Label(frame, text="No Image", bg="white").grid(row=0, column=0, rowspan=3, padx=10, pady=10)
        
        Label(frame, text=f"Party Name: {party_name}", font=("helvetica", 14), bg="white").grid(row=0, column=1, sticky=W, padx=10, pady=2)
        Label(frame, text=f"Election Name: {election_name}", font=("helvetica", 14), bg="white").grid(row=1, column=1, sticky=W, padx=10, pady=2)
        Label(frame, text=f"Achievements: {achievements}", font=("helvetica", 14), bg="white", wraplength=800, justify=LEFT).grid(row=2, column=1, sticky=W, padx=10, pady=2)
        
        vote_button = Button(frame, text="Vote", command=lambda: self.vote(candidate_id), font=("helvetica", 14), bg="blue", fg="white")
        vote_button.grid(row=3, column=0, columnspan=2, pady=10)

        if self.voted_candidate_id and self.voted_candidate_id[0] == candidate_id:
            vote_button.config(state=DISABLED, text="Voted")

    def vote(self, candidate_id):
        if self.voted_candidate_id:
            messagebox.showerror("Error", "You have already voted", parent=self.window)
            return

        conn = mysql.connector.connect(
            host=cr.host,
            user=cr.user,
            password=cr.password,
            database=cr.database
        )
        cursor = conn.cursor()

        # Check if user exists in student_regist
        cursor.execute('SELECT user_id FROM student_regist WHERE user_id=%s', (self.user_id,))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Invalid user ID", parent=self.window)
            conn.close()
            return

        # Fetch the party name of the candidate
        cursor.execute('SELECT party_name FROM can_dashboard WHERE id=%s', (candidate_id,))
        result = cursor.fetchone()
        if result:
            party_name = result[0]
            print(f"Debug: Party Name for candidate {candidate_id} is {party_name}")  # Debug statement

            try:
                print(f"Inserting vote: user_id={self.user_id}, candidate_id={candidate_id}, party_name={party_name}")  # Debug statement
                cursor.execute('INSERT INTO votes (user_id, candidate_id, party_name) VALUES (%s, %s, %s)', (self.user_id, candidate_id, party_name))
                conn.commit()
                messagebox.showinfo("Success", "Vote recorded successfully", parent=self.window)
                self.voted_candidate_id = (candidate_id,)
                self.load_candidate_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"An error occurred: {e}", parent=self.window)
            finally:
                conn.close()
        else:
            messagebox.showerror("Error", "Candidate not found", parent=self.window)
            conn.close()

    def logout(self):
        self.window.destroy()
        import login_page
        root = Tk()
        obj = login_page.login_page(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    user_id = "some_user_id"  # Replace with actual user_id
    obj = UserDashboard(root, user_id)
    root.mainloop()