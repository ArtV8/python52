import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk


def create_window():

    window = tk.Tk()
    window.title("Простое окно")
    window.geometry("1200x1400")

    label = tk.Label(window, text="Это надпись прямо здесь")
    label.place(x=220, y=700)

    image = Image.open("C:\\Users\\User\\OneDrive\\Изображения\\Скрины гта 5\\image.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(window, image=photo)
    label.image = photo
    label.pack()



    window.mainloop()

create_window()

