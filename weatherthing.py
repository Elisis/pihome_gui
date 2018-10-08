import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=melbourne'
json_data = requests.get(api_address.json())
format_add = json_data['base']
print(format_add)
