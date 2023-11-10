import tkinter as tk

from tkinter import Frame, Label, Entry, Button, END, W



# Create tkinter object

app = tk.Tk()

app.geometry("450x450")

# Tambahkan judul

app.title("Kalkulator Luas dan Keliling Persegi Panjang")



# Windows

frame = Frame(app)

frame.pack(padx=20, pady=20)



app.mainloop()