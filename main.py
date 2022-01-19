"""
GUI Application to generate 
qrcode as image
"""

from pyqrcode import create
import tkinter as tk

root = tk.Tk()
root.title('QRC Generator')
data = tk.Entry(root)


def gen_qr():
    global dta
    dta = data.get()
    dta = create(dta)
    test = dta.xbm(scale=5)
    global xbm_image
    xbm_image = tk.BitmapImage(data=test, foreground="black", background='white')
    image_view.config(image=xbm_image)
    statement.config(text="This is a qr code for : " + str(data.get()))


heading = tk.Label(root, text="QR code Generator", font="times 40")
subtitle = tk.Label(root, text="Enter the data ", font="times 20")
make_button = tk.Button(root, text=" Make QR", font="times 20", command=gen_qr)
image_view = tk.Label(root)
statement = tk.Label(root)

# gui grid

heading.grid(row=0, column=0, columnspan=2)
subtitle.grid(row=1, column=0)
data.grid(row=1, column=1)
make_button.grid(row=2, column=0, columnspan=2)
image_view.grid(row=3, column=0, columnspan=2)
statement.grid(row=4, column=0, columnspan=2)

root.mainloop()
