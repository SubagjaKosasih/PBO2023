import tkinter as tk
from tkinter import filedialog
import pygame

root = tk.Tk()
root.title("MP3 Player")

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)
    label_now_playing.config(text=f"Sedang diputar: {filename}")

def stop_music():
    pygame.mixer.music.stop()
    label_now_playing.config(text="Musik dihentikan")

def choose_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    label_selected_file.config(text=f"File MP3 terpilih: {filename}")

label_name = tk.Label(root, text="SUBAGJA KOSASIH")
label_name.pack()

label_name = tk.Label(root, text="220511022")
label_name.pack()

button_choose = tk.Button(root, text="Pilih File MP3", command=choose_file)
button_choose.pack(pady=10)

label_selected_file = tk.Label(root, text="File MP3 terpilih: ")
label_selected_file.pack()

label_now_playing = tk.Label(root, text="Tidak ada musik yang diputar")
label_now_playing.pack(pady=10)

button_play = tk.Button(root, text="Putar", command=play_music)
button_play.pack(pady=5)

button_stop = tk.Button(root, text="Stop", command=stop_music)
button_stop.pack(pady=5)

root.mainloop()
