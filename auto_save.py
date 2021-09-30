import tkinter as tk
import os


# import auto_save_function


# body
window = tk.Tk()
window.title("Auto Save Calculator")
window.maxsize(350, 500)


label = tk.Label(text="Auto Save")
label.pack()

# Amount in bank
question1 = tk.Label(text="How much is in your bank?")
question1.pack()
answer1 = tk.Entry()
answer1.pack()

# Percentage of saving
question2 = tk.Label(text="What is the percentage you would like to save?")
question2.pack()
answer2 = tk.Entry()
answer2.pack()

# DISPLAY USE INPUT


def results():
    display1 = tk.Label(text="The amount entered is : ")
    # display2 = tk.Label(text=answer1)

    display1.pack()
    # display2.pack()


submit_button = tk.Button(window, text="Submit", command=results)
submit_button.pack(side='bottom')

# canvas
canvas = tk.Canvas(window, height=500, width=350)
canvas.pack()

# run app
window.mainloop()
