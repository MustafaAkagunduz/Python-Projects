import requests as rq
from tkinter import *

my_api_key = "728377e3ab23b72b3a014461d16f2e7a"
my_image = None  # Global değişken

def get_the_weather(event=None):  # event=None, Enter tuşuna basıldığında otomatik olarak fonksiyonu çalıştırmak için
    global my_image  # Global değişkeni kullanmak için tanımlanmalı
    city = city_input.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api_key}'
    response = rq.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        desc = data['weather'][0]['description']
        result_label.config(text=f"Temperature: {temp_celsius} °C\nDescription: {desc}")



        if 'clear' in desc.lower() and 'sky' in desc.lower():
            image_path = "gunesli.png"  # Güneşli hava resmi
        elif 'rain' in desc.lower():
            image_path = "yagmurlu.png"  # Yağmurlu hava resmi
        elif 'wind' in desc.lower():
            image_path = "ruzgarli.png"  # Rüzgarlı hava resmi
        elif 'cloud' in desc.lower():
            image_path = "bulutlu.png"  # Bulutlu hava resmi
        else:
            image_path = "default.png"  # Diğer durumlar için varsayılan resim

        # Önceki resmi yok etme
        if my_image is not None:
            image_label.config(image='')

        my_image = PhotoImage(file=image_path)
        image_label.config(image=my_image)
        image_label.image = my_image
        image_label.pack()

    else:
        result_label.config(text='Error fetching weather data')

window = Tk()
window.title("What is the weather??")
window.geometry("400x300")
window.config(padx=30, pady=30)

city_label = Label(text="CITY:")
city_label.pack()
city_input = Entry(width=10)
city_input.focus()
city_input.pack()
bring_button = Button(text="Get!!", command=get_the_weather)
bring_button.pack()
result_label = Label()
result_label.pack()

image_label = Label()
image_label.pack()

# Enter tuşuna basıldığında get_the_weather fonksiyonunu çalıştır
window.bind('<Return>', get_the_weather)

window.mainloop()
