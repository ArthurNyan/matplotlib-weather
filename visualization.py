import matplotlib.pyplot as plt

def visualize_weather_data(weather_data: list[dict]):
    """
    Визуализирует данные о погоде:
    - Диаграмму рассеяния температуры по времени.
    - Ящик с усами для температур.

    :param weather_data: Список данных о погоде.
    """
    times = [entry["datetime"] for entry in weather_data]
    temperatures = [entry["temperature"] for entry in weather_data]

    # Создание диаграммы рассеяния
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(times, temperatures, c="blue", alpha=0.6, label="Температура")
    plt.title("Диаграмма рассеяния (Температура по времени)")
    plt.xlabel("Время")
    plt.ylabel("Температура, °C")
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()

    # Построение "ящика с усами"
    plt.subplot(1, 2, 2)
    plt.boxplot(temperatures, vert=False, patch_artist=True)
    plt.title("Ящик с усами (Температура)")
    plt.xlabel("Температура, °C")

    plt.tight_layout()
    plt.show()
