import tkinter as tk
from PIL import ImageTk, Image  
import mainpage

def open_page():

    def MainPage():
        root.destroy()
        mainpage.open_page()

    root = tk.Tk()
    root.title("Model Specs")
    root.geometry("800x850")

    image1 = Image.open("./viz.png")
    image1 = image1.resize((900, 900), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=-100)

    tk.Button(root, text="Okay", bg="#94fff5", command=MainPage).place(x=300, y=710, width=150, height=70)
    root.mainloop()