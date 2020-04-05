from PIL import Image
import os, pyperclip, re, sys, subprocess
from pytesseract import image_to_string
import tkinter as tk
from tkinter import filedialog, Text, StringVar, messagebox, PhotoImage

root = tk.Tk()
root.title('Phone Numbers Extractor')
image_files = []

my_text = StringVar()
my_text.set('No Images Selected')

new_message = StringVar()
new_message.set('')

def image_select():
    files_path = filedialog.askopenfilenames(title='Select Images', filetypes=[('Image file', ('.png','.jpg','.jpeg'))])
    for files in files_path:
        image_files.append(files)
    image_files.sort()
    select_image_label['text'] = str(len(image_files)) + ' Images Selected'
    process_ocr['state'] = 'normal'

def process_image():
    all_text = []

    for filename in image_files:
        try:
            img = Image.open(filename)
            all_text.append(image_to_string(img))
        except:
            continue

    # +91 95959 59595 or 07557575575 or 0-99555 55999
    phone_regex = re.compile(r'''(
        (\+91|0)?                                   # country code
        (\s|-|\.)?                                  # seperator
        (\d{5})                                     # 5 digits
        (\s|-|\.)?                                  # seperator
        (\d{5})                                     # 5 digits
    )''', re.VERBOSE)

    text = str('\n'.join(all_text))

    matches = []
    phone_num = ''

    for groups in phone_regex.findall(text):
        phone_num = ''.join([groups[3], groups[5]])
        matches.append(phone_num)

    if len(matches) > 0:
        distinct_matches = list(dict.fromkeys(matches))

        if len(matches)!=len(distinct_matches):
            message_label['text'] = str(len(matches)-len(distinct_matches)) + ' Duplicates Removed'
        else:
            message_label['text'] = 'No duplicates found!'

        pyperclip.copy('\n'.join(distinct_matches))
        messagebox.showinfo(title='Success', message='Process Complete! \nCopied to Clipboard')
    else:
        messagebox.showerror(title='Error', message='No Phone no. was found!!')

canvas = tk.Canvas(root, height=400, width=400, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

main_label = tk.Label(frame, text='Phone Numbers Extractor', padx=10, pady=5)
main_label.pack()

select_images = tk.Button(frame, text='Select Images', padx=10, pady=5, fg='#263D42', command=image_select)
select_images.pack()

select_image_label = tk.Label(frame, text=my_text.get(), padx=10, pady=5)
select_image_label.pack()

process_ocr = tk.Button(frame, text='Process Phone Nos.', padx=10, pady=5, fg='#263D42', command=process_image, state='disabled')
process_ocr.pack()

message_label = tk.Label(frame, text=new_message.get(), padx=10, pady=5)
message_label.pack()

exit_button = tk.Button(frame, text='Exit', padx=10, pady=5, fg='#263D42', command=root.destroy)
exit_button.pack()

root.mainloop()
