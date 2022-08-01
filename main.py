import requests
import datetime

#Make 2 variables user_id and user_apiid (strings) (Do not include in final version)
#Make sure to request Imperial
#Will receive in JSON and must convert

#user_id= 'jsando10'
user_zip=''
user_apiid = ''


response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+user_zip+",us&appid="+user_apiid+"&units=imperial")

results = response.json()


print("Name: "+results["name"] + "\n")
print("Current Temp: "+ str(results["main"]["temp"]) + "degrees Fahrenheit\n")
print("Atmospheric Pressure: "+ str(results["main"]["pressure"]) + " hPa\n")
print("Wind Speed: "+ str(results["wind"]["speed"]) + " mph\n")
print("Wind Direction: "+ str(results["wind"]["deg"]) + "\n")
print("Time of Report: "+ str(datetime.datetime.fromtimestamp(results["dt"])) + "\n")