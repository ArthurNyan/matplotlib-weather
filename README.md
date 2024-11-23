# Weather Visualization

Приложение для получения и визуализации данных о погоде за последние 5 дней, используя API OpenWeatherMap.

[Github Gists](https://gist.github.com/ArthurNyan/1500152b0aece6495d7844fed746e040)

## Описание

Проект получает данные о погоде через OpenWeatherMap API и визуализирует их:

- **Диаграмма рассеяния**: температура по времени.
- **Ящик с усами**: разброс температур.

## Установка

### Шаг 1: Клонирование репозитория

```bash
    git clone https://github.com/your-repo/weather_visualization.git
    cd weather_visualization
```

### Шаг 2: Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```bash
    poetry install
    poetry shell
```

### Шаг 3: Получение API-ключа

- Зарегистрируйтесь на OpenWeatherMap.
- Создайте API-ключ в разделе API keys.
- Добавьте ключ в main.py:

```python
    API_KEY = "ваш_ключ_API"
```

### Запуск

Для запуска проекта выполните:

```bash
    python main.py
```
