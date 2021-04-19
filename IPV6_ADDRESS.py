from tkinter import *
from ipv6_address_tools import Address

class Address_GUI:
    def __init__(self, master):
        self.master = master
        master.title = "Address IPV6 GUI"
        master.geometry("650x200")

        self.label_ipv6 = Label(master, text="Ipv6 Address")
        self.label_ipv6.grid(row=1, column=1)

        self.input_ipv6 = Entry(master, width=40)
        self.input_ipv6.grid(row=1, column=2)

        self.label_ipv6 = Label(master, text="/ Prefix")
        self.label_ipv6.grid(row=1, column=3)

        self.input_prefix = Entry(master, width=40)
        self.input_prefix.grid(row=1, column=4)

        self.label_result = Label(master, text="Network Address")
        self.label_result.grid(row=2, column=1)

        self.result = StringVar();
        self.input_result = Entry(master, state=DISABLED, textvariable=self.result, width=40)
        self.input_result.grid(row=2, column=2)

        self.button = Button(master, text="Result", command=self.get_address)
        self.button.grid(row=3, column=2)

        self.message = Label(master, text="")
        self.message.grid(row=4, column=1, rowspan=3)
        

    def get_address(self):
        try:
            full_ipv6 = self.input_ipv6.get()
            prefix = self.input_prefix.get()
            address = Address(full_ipv6, prefix)
            result = address.reseau()
            self.result.set(result + "/" + str(prefix))
            self.message['text'] = "" 
            print(result)  
        except Exception as e:
            self.result.set("")
            self.message['text'] = "Please enter an expanded ipv6 address example: \n Address = 2001:DB8:85A3::8A2E:370:7334 , prefix must be between 0 and 128"   
            print(e)

root = Tk()
gui = Address_GUI(root)
root.mainloop()