
import requests
from typing import Dict, Any, Optional
key = ''
latitude = 5.5
longitude = 8.8






def get_weather(lat: float, lon: float) -> Optional[Dict[str, Any]]:

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric&lang=ru'

    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()

        weather_info = {
            'temperature': round(weather_data['main']['temp'], 1),
            'feels_like': round(weather_data['main']['feels_like'], 1),
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'wind_speed': weather_data['wind']['speed'],
            'description': weather_data['weather'][0]['description'],
            'city': weather_data.get('name', 'Неизвестное место'),
            'country': weather_data.get('sys', {}).get('country', '')
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except KeyError as e:
        print(f"Ошибка при парсинге данных: {e}")
        return None