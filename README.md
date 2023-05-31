# REST API Сотрудники и депортаменты.

Стек: DRF, Docker, Postgres


## Запуск:

```
git clone
```

### Вариант первый через докер

1. В дирректории проекта
```
docker-compose build
docker-compose up -d
```
2. Зайти в веб контейнер и создать пользователя

```
python manage.py createsuperuser
```

### Вариант второй 

1. В дирректории проекта создать виртуальное окружение с учетом вашей ОС:

```
python -m venv venv
```

2. Загрузить зависимости:

```
pip install requirements.txt
```

3. Создать и применить миграции в базу данных:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Запустить сервер

```
python manage.py runserver
```

## доп настройки

```
если не хочется терять данные из бд, можно раскоментировать volume в docker-compose
но при этом могут возникнуть конфликты по правам, для каждой ОС они разные
```

## пользуемся API через swagger

```
http://0.0.0.0:8000/swagger/
или
http://127.0.0.1:8000/swagger/

```
