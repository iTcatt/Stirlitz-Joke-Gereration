# Stirlitz-Joke-Generation-Bot

## Введение

Данный проект является лабораторной работой по предмету ООП. Это асинхронный бот, написанный на aiogram, который способен генерировать шутки про Штирлица при помощи дообученной модели RUGPT2Medium. Генерация шуток происходит на сервере, который коммуницирует с тг ботом при помощи очередей (RabbitMQ).

## Архитектура проекта

![](/images/architecture.png)

## Структура проекта

* [Bot](/bot/)

    * [bot.py](/bot/bot.py) - запуск бота
    * [config.py](/bot/config.py) - хранение токена 
    * [commandMessages.py](/bot/config.py) - собщения от бота на полученные команды
    * [myKeyboard.py](/bot/myKeyboard.py) - клавиатура
    * [client.py](/bot/client.py) - клиент, который организовывает связь с сервером через очередь

* [Server](/server/)
    
    * [generator.py](/server/generator.py) - генерирует шутку
    * [server.py](/server/server.py) - код сервера
## Презентация 

[Презентация](/joke-generation-bot.pptx) о боте 

## Запуск через docker compose

`docker-compose build` 

`docker-compose up`

