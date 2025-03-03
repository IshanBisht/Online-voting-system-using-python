from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  
import pymysql
import credentials as cr

class AdminDashboard:
    def __init__(self, root):
        self.window = root
        self.window.title("Admin Dashboard")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg="white")

        self.results_button = Button(self.window, text="View Results", command=self.view_results, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.results_button.place(x=20, y=20, width=200, height=40)

        self.results_frame = Frame(self.window, bg="white")
        self.results_frame.place(x=20, y=80, width=1240, height=700)

        self.canvas = Canvas(self.results_frame, bg="white")
        self.scrollbar = Scrollbar(self.results_frame, orient=VERTICAL, command=self.canvas.yview)
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
                candidate_info = f"Candidate Name : {candidate_name}\n Party: {party_name}\n Votes: {vote_count}"

                frame = Frame(self.scrollable_frame, bg="white")
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