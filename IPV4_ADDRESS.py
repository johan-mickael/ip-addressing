import tkinter as tk
from tkinter import ttk
from tkinter import *
import ipv4_address_tools as f

class Window():
    w = tk.Tk()
    def init(self):
        self.lbl1 = ttk.Label(self.w, text='Address')
        self.lbl1.place(x=7, y=10)
        self.t1 = ttk.Entry(width="30")
        self.t1.place(x=60, y=10)
        self.b1 = ttk.Button(self.w,text='Result', command=self.result)
        self.b1.place(x=260, y=10)
        self.message = Label(self.w, text="")
        self.message.place(x=0, y=30)

    def result(self): 
        self.message['text'] = ""
        if self.t1.get() == "":
            self.message['text'] = "Invalid IPv4"
            return None
        try:
            f.checkIpv4Format(self.t1.get(), self)
            f.getClass(self.t1.get())
        except Exception as e:
            self.message['text'] = str(e)
            return None   
        teta = 30
        self.classe = ttk.Label(self.w, text='class')
        self.classe.place(x=7, y=10+teta)
        self.classeV = ttk.Label(self.w, text=f.getClass(self.t1.get()))
        self.classeV.place(x=120, y=10+teta)
        self.masque = ttk.Label(self.w, text='mask')
        self.masque.place(x=7, y=30+teta)
        self.masqueV = ttk.Label(self.w, text=f.getMask(self.t1.get()))
        self.masqueV.place(x=120, y=30+teta)
        self.adresseReseau = ttk.Label(self.w, text='network address')
        self.adresseReseau.place(x=7, y=50+teta)
        self.adresseReseauV = ttk.Label(self.w, text=f.getNetworkAddress(self.t1.get(), f.getMask(self.t1.get())))
        self.adresseReseauV.place(x=120, y=50+teta)
        self.adresseBroadcast = ttk.Label(self.w, text='diffusion address')
        self.adresseBroadcast.place(x=7, y=70+teta)
        self.adresseBroadcastV = ttk.Label(self.w, text=f.getBroadcatAddress(self.t1.get(), f.getMask(self.t1.get())))
        self.adresseBroadcastV.place(x=120, y=70+teta)
        self.premierOrdre = ttk.Label(self.w, text='first address')
        self.premierOrdre.place(x=7, y=90+teta)
        self.premierOrdreV = ttk.Label(self.w, text=f.getFirstOrder(self.t1.get(), f.getMask(self.t1.get())))
        self.premierOrdreV.place(x=120, y=90+teta)
        self.dernierOrdre = ttk.Label(self.w, text='last address')
        self.dernierOrdre.place(x=7, y=110+teta)
        self.dernierOrdreV = ttk.Label(self.w, text=f.getLastOrder(self.t1.get(), f.getMask(self.t1.get())))
        self.dernierOrdreV.place(x=120, y=110+teta)
        self.hote = ttk.Label(self.w, text='Host')
        self.hote.place(x=7, y=130+teta)
        self.hoteV = ttk.Label(self.w, text=f.hostBit(self.t1.get()))
        self.hoteV.place(x=120, y=130+teta)
        self.nombreAdresse = ttk.Label(self.w, text='Address valid')
        self.nombreAdresse.place(x=7, y=150+teta)
        self.nombreAdresseV = ttk.Label(self.w, text=f.getAddressNumber(self.t1.get()))
        self.nombreAdresseV.place(x=120, y=150+teta)

    def show(self):
        self.w.geometry('540x600')
        self.init()
        self.w.mainloop()        
        
class Main():
    def main():
        Window().show()
    if __name__ == '__main__':
        main()