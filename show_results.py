import tkinter as tk
import numpy as np
import pandas as pd
import pickle
import mainpage

def preprocess_data(combo_values, number_students, pretest_scores):
    """This function will rearrange the attributes for input
    and fills 0 where <Blank> is given."""
    
    (*reindexed,) = combo_values[0], combo_values[2], combo_values[1], \
                    combo_values[3], combo_values[4], combo_values[5], \
                    number_students,  pretest_scores

    for i, data in enumerate(reindexed):
        if data == "<Blank>": reindexed[i] = 0
    return reindexed



def show_gui(pred, combo_values, number_students, pretest_scores):
    root = tk.Tk()
    root.title("Prediction")
    root.geometry("900x600")
    root.resizable(0, 0)

    left_frame = tk.Frame(root, width=400, height=600)
    left_frame.place(x=0, y=0)
    right_frame = tk.Frame(root, width=500, height=600)
    right_frame.place(x=400, y=0)

    def open_mainpage():
        root.destroy()
        mainpage.open_page()

    def put_label(text, size, weight, x, y, frame=left_frame):
        tk.Label(frame, text=text, 
                font=("Neuville", size, weight)).place(x=x, y=y)

    put_label("__", 20, "bold", 30, 70)
    put_label("Based on your inputs", 20, "bold", 30, 50)

    put_label("Your school is:", 10, "", 30, 120)
    put_label(combo_values[0], 10, "bold", 30, 140)
    
    put_label("Your school type is:", 10, "", 30, 170)
    put_label(combo_values[1], 10, "bold", 30, 190)

    put_label("Your school setting is:", 10, "", 30, 220)
    put_label(combo_values[2], 10, "bold", 30, 240)

    put_label("Your teaching method is:", 10, "", 30, 270)
    put_label(combo_values[3], 10, "bold", 30, 290)

    put_label("Your gender is:", 10, "", 30, 320)
    put_label(combo_values[4], 10, "bold", 30, 340)

    put_label("Your lunch type is:", 10, "", 30, 370)
    put_label(combo_values[5], 10, "bold", 30, 390)

    put_label("Number of students in class:", 10, "", 30, 420)
    put_label(number_students, 10, "bold", 30, 440)

    put_label("Your marks in previous exam was:", 10, "", 30, 470)
    put_label(pretest_scores, 10, "bold", 30, 490)

    tk.Label(root, text="You are supposed\nto get",
                    font=("Neuville", 12, "bold")).place(x=300, y=300)

    put_label(pred, 150, "bold", x=150, y=150, frame=right_frame)
    put_label("M A R K S", 30, "bold", x=170, y=350, frame=right_frame)

    tk.Button(root, text="Okay", bg="#16da75", font=("Neuvillie", 10), command=open_mainpage).place(x=710, y=540, width=200, height=70)

    root.mainloop()



def open_page(combo_values, number_students, pretest_scores):
    """This function will be called from predicting.py
    and will predict the testscores from the given attributes.
    """

    reindexed = preprocess_data(combo_values, number_students, pretest_scores)
    categorical = reindexed[:-2]    
    numerical = reindexed[-2:]    

    with open(r"./model", "rb") as file:
        model = pickle.load(file)
    with open(r"./encoder", "rb") as file:
        encoder = pickle.load(file)

    encoded = encoder.transform([categorical]).toarray()
    pred = model.predict(np.c_[encoded, [numerical]])[0]
    pred = round(pred)
    if pred > 100: pred = 100
    if pred < 0: pred = 0
    
    show_gui(pred, combo_values, number_students, pretest_scores)
    

if __name__ == "__main__":
    show_gui(100, ['GOOBU', 'Urban', 'Public', '<NA>', 'Male', '<NA>'], 22,  0)