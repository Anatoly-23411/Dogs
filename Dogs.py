
from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response
from pygame.examples.cursors import image


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data.response.json()
        return data("message")
    except Exception as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")
        return None





def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img.data = BytesIO(response.content)
            img = Image.open(img.data)
            img.thumbnail(300, 300)
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")





window = Tk()
window.title("Картинки с собачками")
window.geometry(360*420)


label = Label()
label.pack(pady=10)


button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()

