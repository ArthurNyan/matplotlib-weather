import requests
import datetime

def fetch_weather_data(api_key: str, city: str) -> list[dict]:
    """
    Получает данные о погоде за последние 5 дней из API OpenWeatherMap.

    :param api_key: API ключ для доступа к сервису.
    :param city: Название города для запроса.
    :return: Список данных о погоде (с температурой, временем и другими параметрами).
    """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    weather_data = [
        {
            "datetime": datetime.datetime.fromtimestamp(entry["dt"]),
            "temperature": entry["main"]["temp"]
        }
        for entry in data["list"]
    ]
    return weather_data
