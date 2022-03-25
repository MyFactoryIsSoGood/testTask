# testTask
В качестве тестового задания написано приложение, позволяющее искать видео на YouTube, просматривать их, и переводить информацию о них на разные языки.


Используемые сервисы:
1. YouTube Data API v3
2. Yandex Cloud Translate API

Количество запросов:

YouTube:
1. GET https://www.googleapis.com/youtube/v3/search Для получения поисковой выдачи
2. GET https://www.googleapis.com/youtube/v3/videos Для получения информации о видео
          
Yandex:
1. POST https://translate.api.cloud.yandex.net/translate/v2/translate Для перевода данных о видео

База данных PostgreSQL используется для сохранения информации о видео, которые когда-то были найдены. Реализовано, как веб-сервер. Из прочего: сделан минимальный фронт при помощи классов bootstrap.

Потрачено примерно 10 часов на создание приложения.
