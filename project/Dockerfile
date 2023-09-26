# Образ на основе которого создаём контейнер
FROM python:3.11-alpine

# Рабочая директория внутри проекта
WORKDIR /usr/src/project

# Переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копируем содержимое текущей папки в контейнер
COPY . .

# Устанавливаем зависимости (включая make) and пакеты Python
RUN apk add --no-cache g++ make && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Собираем динамическую библиотеку
RUN cd cpp_lib && make
