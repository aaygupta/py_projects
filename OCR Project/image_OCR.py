from PIL import Image
import os, pyperclip
from pytesseract import image_to_string

path = os.path.dirname(os.path.realpath(__file__))
input_path = path + '/Input/'

f = []
t = []

for root, dirs, filenames in os.walk(input_path):
    for filename in filenames:
        try:
            f.append(filename)
            img = Image.open(input_path + filename)
            text = image_to_string(img)
            t.append(text)
        except:
            continue


pyperclip.copy('\n'.join(t))