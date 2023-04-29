import requests #Requires external installation
import json
import os
import pyttsx3

os.system('cls')
city=input("Enter the name of city: ")

url=f"https://api.weatherapi.com/v1/current.json?key=e2fc15f58cdb4d5bbeb35515232603&q={city}"  #use this link to check data on web

x=requests.get(url)
wdic= json.loads(x.text) #to parse data as a dictionary
print(wdic['current']['temp_f'])  

engine = pyttsx3.init()
engine.say(f"Temprature in {city} is {wdic['current']['temp_f']} degree fahrenhite and {wdic['current']['temp_c']} degree celcius")
engine.runAndWait()