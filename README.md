# Django-REST-api

Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

Результат выполнения задачи:
- исходный код приложения в github (только на github, публичный репозиторий)
- инструкция по разворачиванию приложения (в docker или локально)
- документация по API


# Решение:
1. Create virtualenv and activate it

2. pip install -r requirements.txt

3. python manage.py runserver

4. See http://127.0.0.1:8000/redoc/

Тестовый админ(логин/пароль):http://127.0.0.1:8000/admin   test/test1234 


Юзер может авторизироваться по эндпойнту:

POST http://127.0.0.1:8000/api/v1/login

В ответе приходит токен для юзера, вы должны потом во все запросы вставлять этот токен, это как бы постоянная авторизация, то есть во всех следующих запросах в header вы вставляете Content-type и Autorization. Все остальные запросы вы можете посмотреть в redoc, там создать опрос, получить список всех опросов, изменить опрос, создать ответ, ответ создается от текущего юзера, то есть я его определяю по токену и вставляю в ответ, ну и получить список ответов по id пользователя.
Swagger просто показывает все эндпойнты сам, то есть сам смотрит в код и определяет эндпойнты, это делается как документация онлайн.
Смотрите, как я бы объяснял как это работает. Залогинились как какой то пользователь, я создание пользователя не делал, создать можно через админку или через терминал.

Эндпойнт создание опроса

http://127.0.0.1:8000/api/v1/quiz/create_quiz

{
"name": "string",
"start_date": "2020-05-20",
"end_date": "2020-05-20",
"desсription": "string",
"questions": [
0
]
}

name это любое название, даты и questions надо указать id уже ранее созданного вопроса
потом есть PUT и PATCH 

http://127.0.0.1:8000/api/v1/quiz/change_quiz/{id} 

для изменения опроса, вы там уже не можете изменить дату создания, то есть дата создания получается один раз при создании опроса, там можно сделать автоматическое добаление default=datetime.now

Ну и эндпойнт для ответа на вопрос, то есть это какой то пользователь отвечает на вопрос

POST http://127.0.0.1:8000/api/v1/quiz/create_answer

Там видите все поля указаны, но надо по существу заполнить какой то один
{
"text_answer": "string",
"one_answer": 0,
"multiple_answer": [
0
],
"question": 0
}
и указать id вопроса к которому относится ответ

Делается еще один эндпойнт для получения списка всех вопросов, например относящихся к определенному опросу. На фронтенеде получается этот список и в каждом вопросе будет указан тип вопроса (у нас же там есть тип вопроса), и когда фронтендщик выводит все вопросы, относящиеся к какому либо опросу, то он смотрит какой тип у конкретного вопроса и отображает только в таком виде, в каком надо отобразить. Например если выбор из одного ответа, то там будет выпадающее меню с выбором, если множественный выбор, то еще что то. То есть как это преподнести пользователю это делается на фронтенде

последний эндпойнт это

http://127.0.0.1:8000/api/v1/quiz/list_answer/{id}

где id это id какого либо пользователя, он возвращает вам список всех ответов пользователя по всем вопросам, что он когда либо отвечал
