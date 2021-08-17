import tkinter as tk
from tkinter import ttk, messagebox
import predicting

def open_page():
    root = tk.Tk()
    root.title("Provide Attributes")
    root.geometry("490x646")

    frame = tk.Frame(width=500, height=750)
    frame.pack(pady=20, padx=30)


    def get_values():
        nonlocal selections

        combo_values = []
        for combo in selections:
            combo_values.append(combo.get())
        if not all(combo_values):
            messagebox.showerror("Values not selected", 
                                "Please select values from the dropbox.")
        
        else:
            try:
                pretest_scores = int(pretest.get())
                number_students = int(n_studetns.get())
                if not 0 <= number_students <= 100:
                    messagebox.showerror("Wrong Number", "Please choose number of students 0 to 100")
                    return
                root.destroy()
                predicting.open_page(combo_values, number_students, pretest_scores)
            except:
                messagebox.showerror("Wrong Data", "Please don't write. Or write numbers!")



    selections = []
    def set_combobox_and_labels(data, label_value, labelx, labely):
        """This function will set the label and the combobox
        with the given data. Like:
            
        Label
        ______________
        |            |
        —————————————
        """
        nonlocal selections

        tk.Label(frame, text=label_value, font=("Neuville", 10)).place(x=labelx, y=labely)
        combo = ttk.Combobox(frame, values=data)
        combo.config(state="readonly")
        combo.place(x=labelx, y=labely + 20)
        selections.append(combo)

    tk.Label(root, text="Insert Attributes", font=("Neuville", 20)).place(x=130, y=10)
    
    schools = ['ANKYI', 'CCAAW', 'CIMBB', 'CUQAM', 'DNQDD', 'FBUMG', 'GJJHK', 'GOKXL',
            'GOOBU', 'IDGFP', 'KFZMY', 'KZKKE', 'LAYPA', 'OJOBU','QOQTS', 'UAGPU', 
            'UKPGS', 'UUUQX', 'VHDHF', 'VKWQH', 'VVTVA','ZMNYA', 'ZOWMK', "<Blank>"]
    set_combobox_and_labels(schools, "School", 20, 50)

    school_types = ['Non-public', 'Public', "<Blank>"]
    set_combobox_and_labels(school_types, "School Type", 250, 50)

    school_settings = ['Urban', 'Suburban', 'Rural', "<Blank>"]
    set_combobox_and_labels(school_settings, "School Setting", 20, 150)

    teaching_methods = ['Standard', 'Experimental', "<Blank>"]
    set_combobox_and_labels(teaching_methods, "Teaching Method", 250, 150)

    genders = ['Female', 'Male', "<Blank>"]
    set_combobox_and_labels(genders, "Gender", 20, 250)

    lunches = ['Does not qualify', 'Qualifies for reduced/free lunch', "<Blank>"]
    set_combobox_and_labels(lunches, "Lunch", 250, 250)

    # Spin box
    tk.Label(frame, text="Number of Students", font=("Neuville", 10)).place(x=145, y=320)
    n_studetns = tk.Spinbox(frame, from_= 0, to = 100)
    n_studetns.place(x=140, y=350)

    # Slider
    tk.Label(frame, text="Scored in Pretest", font=("Neuville", 10)).place(x=155, y=420)
    pretest = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, font=("Neuville", 10))
    pretest.set(40)
    pretest.place(x=70, y=440, width=300)

    # RUN
    tk.Button(root, text="RUN", bg="#91ffe8", command=get_values, font=("Neuville", 10)).place(x=0, y=600, width=500, height=50)
    root.mainloop()

if __name__ == "__main__":
    open_page()