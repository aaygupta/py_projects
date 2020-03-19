import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title='Choose an Image file for processing..',
    filetypes=[('Image files', ('.png','.jpg','.jpeg','.svg'))]
)
output_path = os.path.split(file_path)[0]
output_ext = os.path.splitext(file_path)[1]

our_image = Image.open(file_path)
width, height = our_image.size
quart_image = our_image.resize((int(width/3), int(height/2)))
quart_image.save(output_path + '/processed' + output_ext)