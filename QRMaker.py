import tkinter as tk
import pyqrcode
import png
import win32api

from pyqrcode import QRCode
from PIL import Image,ImageTk


class mainWin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("QR Code maker")
        self.geometry("350x350")
        self.resizable(False, False)
        
        self.but = tk.Button(self,text="Create", command=self.createButFunc).grid(padx=10,pady=10)
        self.lineInput = tk.Entry(self)
        self.lineInput.insert(0, "Insert Text")
        self.lineInput.grid(row = 0,column=1)
        
        myMenu = tk.Menu(self)
        self.config(menu=myMenu)
        file_menu = tk.Menu(myMenu)

        myMenu.add_cascade(label="File", menu=file_menu)
        file_menu.add_cascade(label="Print", command=self.printPic)
        file_menu.add_cascade(label="Exit", command=self.destroy)
        
        
    def createButFunc(self):
        st = self.lineInput.get()
        line = pyqrcode.create(st)
        line.png('qrcode.png', scale = 6)
        self.createCanvas('qrcode.png', 198, 198, 75, 125, 100, 100)
        
    def createCanvas(self,img,width,height,x,y,startX,startY):
        
        imgCanvas = tk.Canvas(self, width=width,height=height)
        imgCanvas.place(x=x,y=y)

        image = Image.open(img)
        imgCanvas.image = ImageTk.PhotoImage(image)
        imgCanvas.create_image(startX,startY,image=imgCanvas.image)

    def printPic(self):
        win32api.ShellExecute(0, "print", "qrcode.png", None, ".", 0)

        
if __name__ == "__main__":
    win = mainWin()
    win.mainloop()
    