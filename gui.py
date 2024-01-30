import customtkinter as ctk
import tkinter

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")
Root = ctk.CTk()
Root.geometry("1000x750")
Root.title("Home Page")

frame1 = ctk.CTkFrame(master=Root)
frame1.pack(pady=20,padx=20, fill = 'both')
label = ctk.CTkLabel(master=frame1,text="")
label.pack()
def hello():
    label.configure(text="hello world")
    label.pack()
button1= ctk.CTkButton(master=frame1,command=hello)
Root.mainloop()