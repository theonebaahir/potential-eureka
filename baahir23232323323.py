from tkinter import *
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl = Label(text="hey there", fg="white", bg="#072f5f", width=40)
name_lbl = Label(text="full name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    message = "welcome to the application \ntoday's date is : "
    greet = f"hello {name}\n"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, str(date.today()))

textbox = Text(height=3)
btn = Button(text="begin", command=display, height=1, bg="#1261a0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()
