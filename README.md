# Foodgram - приложение "Продуктовый помощник"

## Описание проекта

Учебный проект от Яндекс.Практикума. 
Сайт, на котором пользователи могут публиковать и редактировать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. 

## Ссылка на задеплоенный проект
https://elijah-yap.sytes.net/

## Аутентификация Admin
Почта: admin@admin.ru
Пароль: admin

## Технологии
python
django
drf
nginx
gunicorn
certbot
dotenv
docker/dockerhub
psycopg
djoser
docker

## Запуск проекта
Для запуска проекта необходимо выполнить следующие действия.

- Т.к. проект выполнен c загрузкой в docker hub образов, достаточно скопировать из репозитория файл docker-compose.production.yml в директорию

- Создать в ней файл `.env`, в котором должны содержаться следующие переменные:
    >POSTGRES_DB=foodgram\
    >POSTGRES_USER=foodgram_user\
    >POSTGRES_PASSWORD= # пароль от БД\
    >DB_NAME=foodgram\

    >SECRET_KEY= # ну оч секретный ключ\
    >ALLOWED_HOSTS= # разрешенные хосты\
    >CSRF_TRUSTED_ORIGINS= # пароль от БД\
    >DEBUG=False\

    DB_HOST=db\
    DB_PORT=5432\

- Выполнить команду в консоли из директории с файлом docker-compose.production.yml:
```bash
sudo docker compose -f docker-compose.production.yml up -d
```

- Дождаться сборки и запуска контейнеров, далее в консоли:
```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/static/. /backend_static/static/
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
sudo docker compose -f docker-compose.production.yml exec backend python manage.py upload
```

## Автор
ILYA OLEYNIKOV
GitHub:	https://github.com/Elijah-iSO
E-mail: oleynikovis@yandex.ru