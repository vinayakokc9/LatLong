
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from ctypes import windll
import tkinter  
import pyglet, os
from LatLong import * 
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

pyglet.font.add_file('fonts/Inter-VariableFont_slnt,wght.ttf')
windll.shcore.SetProcessDpiAwareness(1)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("960x540")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 540,
    width = 960,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    480.0,
    540.0,
    fill="#C7D3DD",
    outline="")

canvas.create_rectangle(
    480.0,
    0.0,
    960.0,
    540.0,
    fill="#E7ECEF",
    outline="")

canvas.create_text(
    583.0,
    66.0,
    anchor="nw",
    text="______________________________________",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    646.5,
    264.68053436279297,
    # 625.4709320068359,
    # 255.68053436279297,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    font=('Inter 14'),
    highlightthickness=0,
    state='disabled', 
    wrap='none'
)
entry_1.place(
    x=533.0,
    # y=228.0,
    y=246.0,
    width=227.0,
    height=35.36106872558594
    # width=184.94186401367188,
    # height=53.36106872558594
)


def findFile():
    entry_1.configure(state='normal')
    if(len(entry_1.get("1.0", "end-1c")) != 0):
        print(entry_1.get("1.0", "end-1c"))
        entry_1.delete("1.0", tkinter.END)

    filename = tkinter.filedialog.askopenfilename(filetypes=(("xlsm files", "*.xlsm"), ("All files", "*.*")))
    #regex for file name and not directory
    entry_1.insert(tkinter.END, filename)
    entry_1.configure(state='disabled')

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=findFile,
    relief="flat"
)
button_1.place(
    x=792.0,
    y=245,
    width=113.04006958007812,
    height=37.0
    # x=771.0,
    # y=227.0,
    # width=135.04006958007812,
    # height=55.36106872558594
)

def start():
    text = entry_1.get("1.0", 'end-1c')
    print(f' h{text}hello')

    if(text == ""):
        canvas.itemconfigure(errorText, text="Please upload a valid Excel file.")
        window.after(3000,lambda: canvas.itemconfigure(errorText, text=""))
        return
    else:
        # dialog saying data is being entered - enable gif
         autopopulate(text)
        # dialog that says data has been entered - disable gif

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start,
    relief="flat"
)
button_2.place(
    x=668.0,
    y=408.0,
    width=103.0,
    height=44.45420837402344
)

statusText = canvas.create_text(
    555.0,
    115.0,
    anchor="nw",
    text="Press Browse and select your FDH Excel file ",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    160.0,
    74.0,
    anchor="nw",
    text="Forage Data Hub",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

canvas.create_text(
    64.0,
    34.0,
    anchor="nw",
    text="Autopopulate Longitude and Latitude",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    241.0,
    227.0,
    image=image_image_1
)

canvas.create_text(
    56.0,
    382.0,
    anchor="nw",
    text="Note: City and state names must be spelled out entirely",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    56.0,
    399.0,
    anchor="nw",
    text="in order to find the appropriate longitude and latitude.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    647.0,
    47.0,
    anchor="nw",
    text="Upload Excel File",
    fill="#000000",
    font=("Inter", 18 * -1)
)

errorText = canvas.create_text(
    620.0,
    370.0,
    anchor="nw",
    text="     ",
    fill="#000000",
    font=("Inter", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
