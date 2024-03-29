import tkinter as tk
from PIL import Image, ImageTk

def button_pressed(event):
    event.widget.config(relief="sunken")

def button_released(event):
    event.widget.config(relief="raised")

root = tk.Tk()
root.configure(background="brown")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Cardiovascular Disease Prediction")

image2 = Image.open('images/20.png')
image2 = image2.resize((w, h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label_l1 = tk.Label(root, text="Cardiovascular Disease Prediction", font=("Times New Roman", 35, 'bold'),
                    background="Brown", fg="white", width=40, height=1)
label_l1.place(x=120, y=2)

def reg():
    from subprocess import call
    call(["python", "heart_registration.py"])

def log():
    from subprocess import call
    call(["python", "heart_login.py"])

def window():
    root.destroy()

button1 = tk.Button(root, text="Login", command=log, width=14, height=1, font=('times', 20, ' bold '), bg="green", fg="white")
button1.place(x=100, y=200)
button1.bind("<ButtonPress>", button_pressed)
button1.bind("<ButtonRelease>", button_released)

button2 = tk.Button(root, text="Register", command=reg, width=14, height=1, font=('times', 20, ' bold '), bg="green", fg="white")
button2.place(x=100, y=300)
button2.bind("<ButtonPress>", button_pressed)
button2.bind("<ButtonRelease>", button_released)

button3 = tk.Button(root, text="Exit", command=window, width=14, height=1, font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=100, y=450)
button3.bind("<ButtonPress>", button_pressed)
button3.bind("<ButtonRelease>", button_released)

root.mainloop()