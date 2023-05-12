import pyqrcode
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def CreateWidgets():
    label = tk.Label(text='Enter text:',bg='beige')
    label.grid(row=0 ,column=1,padx=5,pady=5)

    root.entry =Entry(width=30,textvariable=qrInput)
    root.entry.grid(row=0,column=2,padx=5,pady=5)

    button =Button(width=10,text='Generate',command=QRCodeGenerator,bg='beige')
    button.grid(row=0,column=3,padx=5,pady=5)

    label=Label(text='QR Code: ',bg='beige')
    label.grid(row=1,column=1,padx=5,pady=5)

    root.imageLabel= Label(root, background='beige')
    root.imageLabel.grid(row=2,column=1,columnspan=2,padx=5,pady=5)

def QRCodeGenerator():
    qrString=qrInput.get()
    if qrString!='':
        qrGenerate=pyqrcode.create(qrString)

        qrCodePath = 'C:\\Users\\riyab\\Desktop\\qrcode'
        qrCodeName=qrCodePath + '\\' +qrString +'.png'

        qrGenerate.png(qrCodeName,scale=10)
        image=Image.open(qrCodeName)
        image=image.resize((400,400),Image.ANTIALIAS)
        image =ImageTk.PhotoImage(image)
        root.imageLabel.config(image=image)
        root.imageLabel.photo=image
    else:
        messagebox.showerror("ERROR","ENTER A TEXT")

root=tk.Tk()
root.title("PyQr Generator")
root.geometry('510x500')
root.resizable(False,False)
root.config(background='pink')

qrInput =StringVar()
CreateWidgets()
root.mainloop()
