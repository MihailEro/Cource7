# Трекер полезных привычек

### Для проекта по курсу DOCKER были добавлены файлы 'Dockerfile' и 'Docker-compose'

## Приложения для отслеживания выполнения привычек

## Основная модель
  ### Привычка
  * пользователь
  * место выполнения
  * время выполнения
  * действие
  * связанная привычка (опционально)
  * признак приятной привычки
  * периодичность
  * вознаграждение
  * время на выполнение
  * признак публичности



## Как использовать данный проект?
* Склонировать репозиторий в IDE
  
  В терминале ввести команду:
  ```
  git clone https://github.com/MihailEro/Cource7.git
* Установить вирутальное окружение

  ```
  python3 -m venv venv
  ```
* Активировать виртуальное окружение

  ```
  source venv/bin/activate
  ```
* Установить зависимости

  ```
  pip install -r requirements.txt
  ```
* Создать файл ``.env``. Его необходимо заполнить данными из файла ``.env.sample``
* Создать базу данных.
* Создать и применить миграции

  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

* Запустить сервер

  ```
  python3 manage.py runserver
  ```

* Для работы с периодической задачей необходимо включить брокер redis, celery worker и celery beat

  ```
  sudo systemctl start redis
  celery -A config worker -l info
  celery -A config beat -l info -S django 
  ```
  
* Работу сервера так же можнор осуществить через Docker
  ```
  docker-compose up --build
  ```
  
## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 


```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```
  
## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/docs/
* http://127.0.0.1:8000/redoc/
