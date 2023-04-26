from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


weather=Tk()
weather.title("Weather Application")
weather.geometry("900x500+300+200")

weather.resizable(False,False)


def getweather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")

     #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","Feels","Like",temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

#search box
textfield=tk.Entry(weather,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="#fff")
textfield.place(x=50,y=40)
textfield.focus()

search_button=Button(text="Search",borderwidth=0,border=3,bg="#404040",width=10,font="arial 15 bold",fg="#fff",cursor="hand2",command=getweather)
search_button.place(x=400,y=34)

#logo image
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom frame
frame=Frame(weather,width=800,height=90,bg="#2c32c3")
frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(weather,font="arial 15 bold")
name.place(x=30,y=100)

clock=Label(weather,font="Helvetica 20")
clock.place(x=30,y=130)

#labels
label1=Label(weather,text="Wind",font="Helvetica 16 bold",fg="white",bg="#2c32c3")
label1.place(x=120,y=420)

label2=Label(weather,text="Humidity",font="Helvetica 16 bold",fg="white",bg="#2c32c3")
label2.place(x=250,y=420)

label3=Label(weather,text="Description",font="Helvetica 16 bold",fg="white",bg="#2c32c3")
label3.place(x=430,y=420)

label4=Label(weather,text="Pressure ",font="Helvetica 16 bold",fg="white",bg="#2c32c3")
label4 .place(x=650,y=420)

t=Label(font="arial 70 bold",fg="#ee666d")
t.place(x=400,y=150)

c=Label(font="arial 15 bold")
c.place(x=400,y=250)
w=Label(text="...",font="arial 20 bold",bg="#2c32c3")
w.place(x=120,y=450)
h=Label(text="...",font="arial 20 bold",bg="#2c32c3")
h.place(x=280,y=450)
d=Label(text="...",font="arial 20 bold",bg="#2c32c3")
d.place(x=450,y=450)
p=Label(text="...",font="arial 20 bold",bg="#2c32c3")
p.place(x=670,y=450)
        
    
weather.mainloop()
