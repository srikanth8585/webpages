import requests
from pprint import pprint
API_Key = '744c85a34fe812c60c24c9696ef9b5ca'
city = input("Enter a city:")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url)
pprint(weather_data)