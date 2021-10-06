import tkinter as tk


class myApp:
    def __init__(self, window):
        self.amount_in_bank = tk.Label(
            window, text="How much is in your bank?")

        self.answer_1 = tk.Entry()

        self.percentage_save = tk.Label(
            text="What is the percentage you would like to save?")

        self.answer_2 = tk.Entry()
        self.answer_3 = tk.Entry()

        self.amount_in_bank.place(x=20, y=50)
        self.answer_1.place(x=200, y=50)

        self.percentage_save.place(x=20, y=100)
        self.answer_2.place(x=200, y=130)

        self.answer_3.place(x=100, y=200)

        self.button1 = tk.Button(window, text="Submit", command=self.results)
        self.button1.place(x=250, y=350)

    def results(self):
        self.answer_3.delete(0, 'end')
        self.display1 = tk.Label(text="The amount entered is : ")
        results = self.answer_1.get()
        self.answer_3.insert(tk.END, str(results))


# run app
window = tk.Tk()
my_app = myApp(window)
window.title("Auto Save Calculator")
window.geometry("350x500")
window.maxsize(350, 500)
window.mainloop()
