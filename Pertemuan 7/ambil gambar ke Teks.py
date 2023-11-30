import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract


# Set path to Tesseract executable (replace this with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        text = perform_ocr(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

def perform_ocr(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)

# Initialize Tkinter
root = tk.Tk()
root.title("Extract Text from Image")

# Create Widgets
open_button = tk.Button(root, text="Open Image", command=extract_text)
open_button.pack()

text_box = tk.Text(root, height=15, width=60)
text_box.pack()

# Run the main loop
root.mainloop()
