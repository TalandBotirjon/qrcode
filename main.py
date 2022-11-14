from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Qr code Generator")
root.geometry('500x550')
root.configure(background='#d9ffb3', bg="#59b300")


def create_code():
    input_path = filedialog.asksaveasfilename(title='Save Image', filetyp=(('PNG File', '.png'), ("ALL Files", '*.*')))
    if input_path:
        if '.png' in input_path:
            get_code = pyqrcode.create(my_entry.get())
            get_code.png(input_path, scale=5)
        else:
            input_path = f"{input_path}.png"
            get_code = pyqrcode.create(my_entry.get())
            get_code.png(input_path, scale=5)
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        my_label.config(image=get_image)
        my_entry.delete(0, END)
        my_entry.insert(0, 'Finished')


def clear_all():
    my_entry.delete(0, END)
    my_label.config(image='')


my_entry = Entry(root, font=('Helvetica', 18), background="#ccff99")
my_entry.pack(pady=20)

my_button = Button(root, text='Create Qr Code', background='#ccff99', command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text="Clear", background='#ccff99', command=clear_all)
my_button2.pack(pady=20)


my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()