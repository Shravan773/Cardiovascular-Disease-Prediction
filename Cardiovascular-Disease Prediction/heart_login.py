from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk

class main:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.widgets()

    def login(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                       "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            ms.showinfo("Message", "Login successfully")
            self.master.destroy()
            # Call subprocess
            import subprocess
            subprocess.call(['python', 'heart.py'])
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

    def on_entry_click(self, event):
        """function that gets called whenever entry is clicked"""
        if self.username_entry.get() == "Enter Username":
            self.username_entry.delete(0, "end") # delete all the text in the entry
            self.username_entry.insert(0, '') #Insert blank for user input
            self.username_entry.config(fg = 'black', relief='sunken', bd=1)

    def on_exit_entry(self, event):
        """function that gets called whenever entry is clicked"""
        if self.username_entry.get() == '':
            self.username_entry.insert(0, 'Enter Username')
            self.username_entry.config(fg = 'grey', relief='flat', bd=0)

    def widgets(self):
        # Load the image
        image = Image.open("images/15.jpg")  # Replace "15.jpg" with the path to your image
        image = ImageTk.PhotoImage(image)
        image_label = Label(self.master, image=image)
        image_label.image = image
        image_label.pack(side=LEFT, padx=5, pady=10)

        container = Frame(self.master)
        container.pack(side=RIGHT, fill=BOTH, expand=True)

        # Header
        header_label = Label(container, text="Login", font=("Helvetica", 20))
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Login Frame
        login_frame = Frame(container)
        login_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        Label(login_frame, text='Username:').grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = Entry(login_frame, textvariable=self.username, bg="white", fg="grey", font=("Helvetica", 12), relief='flat')
        self.username_entry.insert(0, 'Enter Username')
        self.username_entry.bind('<FocusIn>', self.on_entry_click)
        self.username_entry.bind('<FocusOut>', self.on_exit_entry)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        Label(login_frame, text='Password:').grid(row=1, column=0, padx=5, pady=5)
        password_entry = Entry(login_frame, textvariable=self.password, show='*', bg="white", fg="grey", font=("Helvetica", 12), relief='flat')
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = Button(login_frame, text='Login', command=self.login, bg="#4CAF50", fg="white", font=("Helvetica", 10), width=10)
        login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Centering the login frame
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

root = Tk()
root.geometry("900x400")  # Adjust window size as needed
root.title("Login Page")
root.resizable(False, False)  # Prevent window from being resized

main(root)

root.mainloop()
