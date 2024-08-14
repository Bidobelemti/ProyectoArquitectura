import requests 
import csv
import os
from datetime import datetime

API_KEY = 'c033c7ed75ebeceee8ad34b9f182524a'
LAT = 52.52437
LON = 13.41053
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'

def get_weather():
    response = requests.get(URL)
    data = response.json()
    return {
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'weather': data['weather'][0]['description']
    }

def write_to_csv(data):
    file_exists = os.path.isfile('clima-berlin-hoy.csv')
    with open('clima-berlin-hoy.csv', 'a', newline='') as csvfile:
        fieldnames = ['datetime', 'temperature', 'humidity', 'pressure', 'weather']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

if __name__ == '__main__':
    weather_data = get_weather()
    write_to_csv(weather_data)