from django.urls import path
from . import views

#app_name register, {% url app_name:view %}
app_name = "template_app" #html dosyasında jinja parantezi açınca url'ye vermek için
# <a href"{% url 'app_name:view_name' %}">click</a> 
# şeklinde kullanmak için
urlpatterns = [
    path("",views.index,name="index"),
    path("weather/",views.weather_view,name="weatherview")
]
