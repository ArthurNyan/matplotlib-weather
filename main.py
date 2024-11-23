from weather_api import fetch_weather_data
from visualization import visualize_weather_data

if __name__ == "__main__":
    # Задайте ваш API ключ и город
    API_KEY = "5ed31e2a1f752172b8251d44d41cf669"
    CITY = "Saint Petersburg"

    try:
        # Получение данных о погоде
        weather_data = fetch_weather_data(API_KEY, CITY)
        
        # Визуализация данных
        visualize_weather_data(weather_data)
    except Exception as e:
        print(f"Ошибка: {e}")
