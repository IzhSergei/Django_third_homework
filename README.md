Для запуска проекта воспользуйтесь командой: python manage.py runserver
Для запуска worker воспользуйтесь командой: celery -A config worker --loglevel=info

на опрерационной системе должн быть запущен redis

В ДЗ реализована фоновая задача по логированию добавления товара.
Сообщения одобавлении товара выводятся в консоль и записываются в файл log.txt 

