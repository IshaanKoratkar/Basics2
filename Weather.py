import json
import requests
from tkinter import *

window = Tk()
window.geometry("1000x450") 
window.title("Weather")  
city_label = Label(window, text = 'Your City') 
city_label.pack()

api_key = "70ee2c91af84e06f66754f876bdc0aef"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = str(input("Enter city name : "))
city_label = Label(window, text = city_name)
city_label.pack()
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial"
response = requests.get(complete_url)
x = response.json()
current_temperature = ""

if x["cod"] != "404": 

    y = x["main"] 
    current_temperature = y["temp"] 
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"] 
    weather_description = z[0]["description"]

    print("Temperature (in Fahrenheit) = " + str(current_temperature))
    print("Atmospheric pressure (in hPa) = " + str(current_pressure))
    print("Humidity (in percents) = " + str(current_humidiy))
    print("Description = " + str(weather_description)) 
    print("URL is " + complete_url)
    
elif x["cod"] == "404":

    print("City not found.")
    print("URL is " + complete_url)



temp_label = Label(window, text = ("Temperature (in Fahrenheit) = " + str(current_temperature)))
temp_label.pack()

window.mainloop()
