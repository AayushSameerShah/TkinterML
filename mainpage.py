import tkinter as tk
import attribute_page
import model_page
import model_viz

# GUI
def open_page():

    # LOGIC
    def open_attributes_page():
        root.destroy()
        attribute_page.open_page()

    def show_model():
        root.destroy()
        model_page.open_page()
    
    def show_viz():
        root.destroy()
        model_viz.open_page()

    root = tk.Tk()
    root.geometry("500x400")
    root.title("Predict your score!")
    root.resizable(0, 0)

    main_label = tk.Label(root, text="Your attributes matter", font= ('Neuville',25, 'bold'))
    main_label.pack(pady=50)

    sum_label = tk.Label(root, text="than your work does", font= ('Neuville',15))
    sum_label.place(x=140, y=100)

    predict_btn = tk.Button(root, text="PREDICT", bg="#69ff9b", font= ('Neuville',15),
                                command=open_attributes_page)
    predict_btn.pack(ipadx=15, ipady=10, pady=50)

    tk.Button(root, text="Show Technicals", bg="#a8ffc5",
                font= ('Neuville',10), command=show_model).place(x=-1, y=365, width=120, height=40)

    tk.Button(root, text="Show Viz", bg="#a8ffc5",
                font= ('Neuville',10), command=show_viz).place(x=390, y=365, width=120, height=40)

    root.mainloop()


if __name__ == "__main__":
    open_page()