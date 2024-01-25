import tkinter as tk
from Karakterbog import Karakterbog
from tkinter import messagebox

class KarakterbogGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.karakterbog = Karakterbog()
        self.title("Karakterbog")

        self.karakter_entry = tk.Entry(self)
        self.karakter_entry.pack()
        self.karakter_entry.bind('<Return>', self.indtast_karakter) 

        self.indtast_button = tk.Button(self, text="Indtast karakter", command=self.indtast_karakter)
        self.indtast_button.pack()

        self.statistik_button = tk.Button(self, text="Beregn statistik", command=self.beregn_statistik)
        self.statistik_button.pack()

        self.clear_karakterer_button = tk.Button(self, text="Ryd karakterer", command=self.clear_karakterer)
        self.clear_karakterer_button.pack()

        self.karakter_listbox = tk.Listbox(self, width=25, height=25)
        self.karakter_listbox.pack()

    def indtast_karakter(self, event=None): 
        karakter = self.karakter_entry.get()
        try:
            karakter = float(karakter)
            error_message = self.karakterbog.indtast_karakter(karakter)
            if error_message:
                messagebox.showerror("Fejl", error_message)
            else:
                self.karakter_entry.delete(0, tk.END)  
                self.karakter_listbox.insert(tk.END, karakter)  
        except ValueError:
            messagebox.showerror("Fejl", "Indtast venligst et gyldigt decimaltal.")

    def beregn_statistik(self):
        statistik = self.karakterbog.beregn_statistik()
        messagebox.showinfo("Statistik", statistik)

    def clear_karakterer(self):
        self.karakterbog.clear_karakterer()
        self.karakter_listbox.delete(0, tk.END)

app = KarakterbogGUI()
app.mainloop()