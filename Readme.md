TestIT Report
=============

Сервис выгрузки тест-кейсов из TestIT по шаблону.
В web интерфейсе доступны 2 поля - выбор проекта и название шаблона (сейчас только Default)
После выбора проекта и нажатии html - формируется html отчёт с кейсами.
Для формирования отчёта требуется длительное время, но мы работаем над этим. ;)


Installation
============

create file .env
```shell script
TOKEN=<TOKEN_FROM_TEST_IT>
URL=<TEST_IT_URL>
```

start container:
```shell script
docker-compose up -d
```

open:
```shell script
http://localhost:5678
```
