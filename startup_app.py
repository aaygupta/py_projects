import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess

root = tk.Tk()
apps = []

if os.path.isfile('startup_apps.txt'):
    with open('startup_apps.txt', 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=[('Apps', '.app')])
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()

def runApps():
    # if sys.platform == "win32":
    #     for app in apps:
    #         os.startfile(app)
    # else:
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    for app in apps:
        subprocess.call([opener, app])


canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(root, text='Open File', padx=10, pady=5, fg='#263D42', command=addApp)
open_file.pack()

run_apps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg='#263D42', command=runApps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('startup_apps.txt', 'w')as f:
    for app in apps:
        f.write(app + ',')