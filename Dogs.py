from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from pygame.examples.cursors import image
from pygame.examples.playmus import Window
from setuptools.windows_support import windows_only

window = Tk()
window.title("Картинки с собачками")
window.geometry(360*420)


label = Label()
label.pack(pady=10)


button = Button(text="Загрузить изображение", command=show-image)
button.pack(pady=10)

window.split()
