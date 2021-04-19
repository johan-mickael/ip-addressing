from tkinter import *
from ipv6_abbreviation_tools import Abbreviation

class Abbreviation_GUI:
    def __init__(self, master):
        self.master = master
        master.title = "Abbreviation IPV6 GUI"
        master.geometry("650x200")

        self.label_ipv6 = Label(master, text="Full IPV6")
        self.label_ipv6.grid(row=1, column=1)

        self.input_ipv6 = Entry(master, width=40)
        self.input_ipv6.grid(row=1, column=2, columnspan=4)

        self.label_result = Label(master, text="Abbreviation")
        self.label_result.grid(row=2, column=1)

        self.result = StringVar();
        self.input_result = Entry(master, state=DISABLED, textvariable=self.result, width=40)
        self.input_result.grid(row=2, column=2)

        self.button = Button(master, text="Result", command=self.get_abbreviation)
        self.button.grid(row=3, column=2)

        self.message = Label(master, text="")
        self.message.grid(row=4, column=1, rowspan=3)

    def get_abbreviation(self):
        try:
            full_ipv6 = self.input_ipv6.get()
            abbreviation = Abbreviation(full_ipv6)
            result = abbreviation.abbreviation()
            self.result.set(result)
            self.message['text'] = "" 
            print(result)  
        except Exception as e:
            self.result.set("")
            self.message['text'] = "Please enter an expanded ipv6 address example: \n 3210:0000:0000:0000:0000:0000:0000:0000"   
            print(str(e))

root = Tk()
gui = Abbreviation_GUI(root)
root.mainloop()