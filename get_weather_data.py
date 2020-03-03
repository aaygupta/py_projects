from OWM_credentials import APP_ID
import json, requests, sys
from datetime import datetime
import dateutil.tz

if len(sys.argv) < 2:
    print('Usage: get_weather_data.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&APPID=%s&units=metric' % (location, APP_ID)
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

print()
print('Presently in %s ' % (location))
print(weather_data['weather'][0]['main'], '-', weather_data['weather'][0]['description'])
print('Current Temp. ', round(weather_data['main']['temp']), '\u00b0C')
print('Feels like ', round(weather_data['main']['feels_like']), '\u00b0C')
print('Min Temp. ', round(weather_data['main']['temp_min']), '\u00b0C')
print('Max Temp. ', round(weather_data['main']['temp_max']), '\u00b0C')
print('Humidity ', weather_data['main']['humidity'], '%')
print('Wind Speed ', round(weather_data['wind']['speed']*3.6), 'Km/h')
print('Sunrise ', datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=dateutil.tz.tzoffset(None,weather_data['timezone'])).strftime('%d-%m-%Y %H:%M:%S'))
print('Sunset ', datetime.fromtimestamp(weather_data['sys']['sunset'], tz=dateutil.tz.tzoffset(None,weather_data['timezone'])).strftime('%d-%m-%Y %H:%M:%S'))
print()