import tkinter as tk
from tkinter.constants import X

app_width = 350
app_height = 500


class myApp:
    def __init__(self, window):

        self.window = window

        self.display_title = tk.Label(text="Welcome to Auto Save")
        self.display_title.place(x=(app_width/3), y=100)
        self.start_button = tk.Button(
            window, text="Start", command=self.after_menu)
        self.start_button.place(x=(app_width/2)-25, y=200)

    def after_menu(self):
        self.start_button.destroy()
        self.amount_in_bank = tk.Label(
            self.window, text="How much is in your bank?")

        self.answer_1 = tk.Entry()

        self.percentage_save = tk.Label(
            text="What is the percentage you would like to save?")

        self.answer_2 = tk.Entry()
        self.answer_3 = tk.Entry()

        self.amount_in_bank.place(x=20, y=50)
        self.answer_1.place(x=200, y=50)

        self.percentage_save.place(x=20, y=100)
        self.answer_2.place(x=200, y=130)

        self.button1 = tk.Button(
            self.window, text="Submit", command=self.results)
        self.button1.place(x=250, y=350)

    def results(self):
        self.answer_3.delete(0, 'end')
        self.display1 = tk.Label(text="The amount entered is : ")
        self.display1.place(x=20, y=170)
        self.answer_3.place(x=200, y=200)
        results = self.answer_1.get()
        if results != "":
            self.answer_3.insert(tk.END, str(results))
        else:
            self.answer_3.insert(tk.END, 0)


# run app
window = tk.Tk()
my_app = myApp(window)
window.title("Auto Save Calculator")
window.geometry("350x500")
window.maxsize(app_width, app_height)
window.mainloop()
