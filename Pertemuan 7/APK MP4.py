import tkinter as tk
from tkinter import filedialog
import cv2

def play_video():
    filename = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if filename:
        cap = cv2.VideoCapture(filename)
        if not cap.isOpened():
            print("Error: Gagal membuka video.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Video Player", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
root.title("Pemutar Video MP4")
label_name = tk.Label(root, text="SUBAGJA KOSASIH")
label_name.pack()

label_name = tk.Label(root, text="220511022")
label_name.pack()
button_choose = tk.Button(root, text="Pilih Video", command=play_video)
button_choose.pack(pady=20)

root.mainloop()
