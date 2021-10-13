import tkinter as tk
from tkinter import Label, ttk
from tkinter import font

app_width = 350
app_height = 500


class myApp:
    def __init__(self, window):
        # the app window
        self.window = window

        # app title
        self.display_title = tk.Label(
            text="Welcome to Auto Save", font=("Arial", 15), background='#5ABFFF', fg="white")
        self.display_title.place(x=(app_width/4)-10, y=100)

        # app start button
        self.start_button = tk.Button(
            window, text="Start", command=self.after_menu, width=20)
        self.start_button.place(x=(app_width/3)-10, y=200)

    # checking if inputs are numbers
    def numbers_only(self):
        self.amount_in_bank_results_dulpicate_output.delete(0, 'end')
        self.percentage_save_dulpicate_output.delete(0, 'end')
        try:
            new_num = float(self.amount_in_bank_results.get())
            self.returning_num1 = round(new_num, 2)
            self.error_message1.destroy()

        except ValueError:
            # error messages
            self.error_message1 = tk.Label(
                text="Please enter a number(s).", background='#5ABFFF', fg="#9B0000")
            self.error_message1.place(x=200, y=70)

    def after_menu(self):
        # clean screen
        self.display_title.destroy()
        self.start_button.destroy()

        # dropdown menu
        self.list_of_options = ('percentage', 'amount')
        self.dropdown_list = tk.StringVar()
        self.list_of_options = ttk.Combobox(
            window, width=10, textvariable=self.dropdown_list, values=self.list_of_options, state="readonly")

        # Amount in bank
        self.amount_in_bank = tk.Label(
            self.window, text="How much is in your bank?")

        self.amount_in_bank_results = tk.Entry()
        self.amount_in_bank.place(x=20, y=50)
        self.amount_in_bank_results.place(x=200, y=50)

        # Amount to save
        self.percentage_save = tk.Label(
            text="How much would you like to save?")

        self.saving_amount = tk.Entry()
        self.saving_amount.place(x=75, y=130)

        # option for amount to save (percentage or amount)
        self.list_of_options.grid(column=1, row=2)

        self.percentage_save.place(x=20, y=100)
        self.list_of_options.place(x=220, y=130)
        self.list_of_options.current(0)

        # submit button
        self.button1 = tk.Button(
            self.window, text="Submit", command=lambda: [self.numbers_only(), self.results()])
        self.button1.place(x=250, y=350)
        self.amount_in_bank_results_dulpicate_output = tk.Entry()
        self.percentage_save_dulpicate_output = tk.Entry()

    def results(self):

        # clearing input bar
        self.amount_in_bank_results_dulpicate_output.delete(0, 'end')
        self.percentage_save_dulpicate_output.delete(0, 'end')

        # Output of user input for amount in bank
        self.output_for_amount_in_bank = tk.Label(
            text="The amount entered is : ")
        self.output_for_amount_in_bank.place(x=20, y=170)
        self.amount_in_bank_results_dulpicate_output.place(x=200, y=170)
        results = self.returning_num1

        # Output of user input for saving
        self.output_for_saving = tk.Label(
            text="The percentage you want to save entered is : ")
        self.output_for_saving.place(x=20, y=200)
        self.percentage_save_dulpicate_output.place(x=200, y=230)
        result_percentage = self.saving_amount.get()

        # checking statement
        if results != "" and result_percentage != "":
            self.amount_in_bank_results_dulpicate_output.insert(
                tk.END, str(results))
            self.percentage_save_dulpicate_output.insert(
                tk.END, str(result_percentage))
        elif results != "" or result_percentage != "":
            self.amount_in_bank_results_dulpicate_output.insert(
                tk.END, str(results))
            self.percentage_save_dulpicate_output.insert(
                tk.END, str(result_percentage))
        else:
            self.amount_in_bank_results_dulpicate_output.insert(tk.END, 0)
            self.percentage_save_dulpicate_output.insert(tk.END, 0)


# run app
window = tk.Tk()

# UX design for app
window.configure(background='#5ABFFF')

my_app = myApp(window)
window.title("Auto Save Calculator")
window.geometry("350x500")
window.minsize(app_width, app_height)
window.maxsize(app_width, app_height)

window.mainloop()
