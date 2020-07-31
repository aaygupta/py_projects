from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os, sys

root = tk.Tk()
root.withdraw()

def open_image(dialog_title):
    file_path = filedialog.askopenfilename(title=dialog_title, filetypes=[('Image file', ('.jpg', '.png', '.jpeg'))])
    if file_path.strip() == '':
        sys.exit()
    img_file = open(file_path, 'rb')
    return img_file

def open_multiple_images(dialog_title):
    files_path = filedialog.askopenfilenames(title=dialog_title, filetypes=[('Image file', ('.jpg', '.png', '.jpeg'))])
    img_files = []
    for files in files_path:
        img_files.append(files)
    img_files.sort()
    return img_files

def save_this_file(dialog_title, dialog_ext):
    file_output = filedialog.asksaveasfile(mode='wb', defaultextension=dialog_ext, title=dialog_title)
    if file_output is None:
        messagebox.showinfo('Error', 'Location Undefined!')
        sys.exit()
    return file_output

def compress_img():
    img_file = open_image('Choose an image for processing..')
    # img_files = open_multiple_images('Choose one or more images for processing..')
    image = Image.open(img_file)
    img_output = save_this_file('Choose the location to Save output Image', '.png')
    image.save(img_output,quality=10)
    img_output.close()
    messagebox.showinfo('Success', 'Image Compression Successful!')

compress_img()