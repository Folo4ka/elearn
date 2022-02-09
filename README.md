## Сайт электронных курсов

### Модули:
- Курсы
- CMS для авторов курсов (/course/mine)
- Онлайн чат студентов курса
- API курсов (по пути /api)

### Установка

> docker-compose up

Миграции (в новом окне терминала)

> docker-compose exec app python manage.py migrate

Далее создаете суперпользователя из корня проекта:
> python manage.py createsuperuser

Теперь можете по адресу localhost:8000/admin войти в админку
Далее по пути /course/mine можете заполнять курсы