from tkinter import *
import time
import os
import show_results

def open_page(combo_values, number_students, pretest_scores):
    root = Tk()
    root.title("Mysterious calculations")
    root.geometry("400x400")
    root.resizable(0, 0)
    root.config(bg="white")

    PATH = r"./giphy.gif"
    frameCnt = 24
    frames = [PhotoImage(file=PATH, format='gif -index %i' %(i)) for i in range(frameCnt)]

    
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)

    
    label = Label(root, bg="white")
    label.pack(pady= 50)
    root.after(0, update, 0)


    status = Label(root, text="", bg="white",
            font=("Neuville", 20, "bold"))
    status.pack()


    def get_new_text():
        text = ["Taking Attributes", "Applying Transformations", "Checking Data", 
                "Assigning Agreement", "Calculating Calculus", "Calculating Calculus", 
                "Checking Parameters", "Oh it's Rocket Science", "I can do that!",
                "Easy...", "Just a sec.", "Done!"]
        for i in text: yield i

    new_text = get_new_text()


    def Refresher():
        try:
            status.configure(text=next(new_text))
            root.after(1000, Refresher) # every second...
        except:
            root.destroy()
            show_results.open_page(combo_values, number_students, pretest_scores)

    Refresher()
    root.mainloop()