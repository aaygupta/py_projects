# pip install pyperclip
import pyperclip, webbrowser, sys

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)