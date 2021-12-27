
import requests

response = requests.get("http://openweathermap.org")
json = response.json
print(json)
