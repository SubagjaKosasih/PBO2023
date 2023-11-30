import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os

root = tk.Tk()
root.title("Text to Speech")

def convert_text_to_speech():
    text = entry_text.get()
    language = 'en'  # Ganti dengan kode bahasa yang diinginkan, misal 'id' untuk Bahasa Indonesia

    # Membuat objek gTTS dengan teks yang diinput dan bahasa yang dipilih
    tts = gTTS(text=text, lang=language, slow=False)

    # Simpan audio dalam file temp.mp3
    tts.save("temp.mp3")

    # Mainkan audio
    playsound("temp.mp3")

    # Hapus file audio setelah diputar
    os.remove("temp.mp3")
    
label_name = tk.Label(root, text="SUBAGJA KOSASIH")
label_name.pack()

label_name = tk.Label(root, text="220511022")
label_name.pack()

label = tk.Label(root, text="Masukkan teks yang ingin diubah menjadi suara:")
label.pack()

entry_text = tk.Entry(root, width=50)
entry_text.pack()

button_convert = tk.Button(root, text="Convert to Speech", command=convert_text_to_speech)
button_convert.pack(pady=10)

root.mainloop()
