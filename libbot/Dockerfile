# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы (echobot.py, config.py)
COPY . .

# Команда для запуска бота
CMD ["python", "echobot.py"]