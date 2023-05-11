![foodgram Workflow Status](https://github.com/Anatoliy-Babenkov/foodgram-project-react/actions/workflows/main.yml/badge.svg)
<h1><p align="center"> 𝔽𝕠𝕠𝕕𝔾𝕣𝕒𝕞 ℙ𝕣𝕠𝕛𝕖𝕔𝕥 </p></h1>

<h2><p align="center"> Описание проекта: </p></h2>

<b>«Продуктовый помощник»</b> - онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
<br>

<h2><p align="center"></p></h2>

<h2><p align="center">Как запустить проект:</p></h2>

<b>1.</b> Скопировать репозиторий:
```
git clone git@github.com:Anatoliy-Babenkov/foodgram-project-react.git
```
<b>2.</b> Cоздать и активировать виртуальное окружение:
* <i>Linux</i>:
```
  source venv/bin/activate
```
* <i>Windows</i>:
```
  source venv/Scripts/activate
```
<b>3.</b> Обновить <i>PIP</i>:
```
python -m pip install --upgrade pip
```
<b>4.</b> Установить зависимости из <i>requirements.txt</i>:
```
pip install -r backend/requirements.txt
```
<b>Необходимо установить:</b>
* <a href=https://www.docker.com/get-started>Docker</a>
* <a href=https://docs.docker.com/compose/install/>Docker-compose</a>

<b>5.</b> Из папки проекта <i>Infra</i> ввести команду:
```
docker-compose up --build
```
<b>6.</b> Провести миграцию базы данных:
```
docker-compose exec backend python manage.py migrate
```
<b>7.</b> Создать суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
<b>8.</b> Провести сбор статики:
```
docker-compose exec backendpython manage.py collectstatic --no-input
```
<h2><p align="center"></p></h2>

<h2><p align="center">После запуска, подробная информация о использовании:</p></h2>
<p align="center"><a href=http://0.0.0.0/redoc/>Redoc</a></p>
<h2><p align="center"></p></h2>

<h2><p align="center">При использовании <i>Github: Actions</i>:</p></h2>
Необходимо создать Secrets со следующими данными:

<br>
<br>

* <b>DB_ENGINE</b>: Двигатель адаптера базы данных (django.db.backends.postgresql);
* <b>DB_HOST</b>: Хост базы данных (db);
* <b>DB_NAME</b>: Название базы данных (postgres);
* <b>DB_PORT</b>: Порт для базы данных (5432);
* <b>DOCKER_PASSWORD</b>: Пароль пользователя Docker;
* <b>DOCKER_USERNAME</b>: Пользователь Docker;
* <b>HOST</b>: Адрес сервера для запуска проекта;
* <b>POSTGRES_PASSWORD</b>: Пароль пользователя базы данных (postgres);
* <b>POSTGRES_USER</b>: Пользователь базы данных (postgres);
* <b>SSH_KEY</b>: Ключ для входа на сервер запуска проекта;
* <b>TELEGRAM_TO</b>: ID Telegram куда следует направить отчёт об успешном запуске;
* <b>TELEGRAM_TOKEN</b>: ID Telegram бота длч отправки;
* <b>USER</b>: Пользователь для входа на сервер запуска проекта;

<h2><p align="center"></p></h2>

<h2><p align="center">Автор кода <i>api_yamdb</i>:</p></h2>

<br>
<br>

<p align="center"><a href=https://github.com/Anatoliy-Babenkov>Бабенков Анатолий</a></p>