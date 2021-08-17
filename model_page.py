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

    image1 = Image.open("./Transparent.png")
    image1 = image1.resize((800, 350), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=0)

    y = 450
    tk.Label(root, text="Model: ", font=("Neuville", 15, 'bold')).place(x=30, y=y)
    tk.Label(root, text="Multiple Linear Regression", font=("Neuville", 15)).place(x=110, y=y)

    tk.Label(root, text="Algorithm: ", font=("Neuville", 15, 'bold')).place(x=30, y=y+40)
    tk.Label(root, text="Least Squared Error", font=("Neuville", 15)).place(x=140, y=y+40)

    tk.Label(root, text="Input Params: ", font=("Neuville", 15, 'bold')).place(x=30, y=y+80)
    tk.Label(root, text="36", font=("Neuville", 15)).place(x=180, y=y+80)

    tk.Label(root, text="_____", font=("Neuville", 15, 'bold')).place(x=420, y=390)
    tk.Label(root, text="Positively Correlated Attributes", font=("Neuville", 15, 'bold')).place(x=420, y=370)

    
    y2 = 370
    tk.Label(root, text="1. Teaching Method Expernimental →    3.057", font=("Neuville", 12)).place(x=420, y=y2+60)
    tk.Label(root, text="2. School Name UKPGS →    2.88", font=("Neuville", 12,)).place(x=420, y=y2+100)
    tk.Label(root, text="3. School Name IDGFP →    2.74", font=("Neuville", 12)).place(x=420, y=y2+140)


    tk.Label(root, text="_____", font=("Neuville", 15, 'bold')).place(x=420, y=630)
    tk.Label(root, text="Negatively Correlated Attributes", font=("Neuville", 15, 'bold')).place(x=420, y=600)

    
    y3 = 640
    tk.Label(root, text="1. Teaching Method Standard →    -3.057", font=("Neuville", 12)).place(x=420, y=y3+40)
    tk.Label(root, text="2. School Name KFZMY →    -2.97", font=("Neuville", 12,)).place(x=420, y=y3+80)
    tk.Label(root, text="3. School Name VVTVA →    -2.08", font=("Neuville", 12)).place(x=420, y=y3+120)
    
    tk.Button(root, text="Okay", bg="#94fff5", command=MainPage).place(x=30, y=710, width=150, height=70)

    root.mainloop()