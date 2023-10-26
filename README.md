
# sms_reminder
Приложение для отправки смс-уведомлений в определенное время каждый месяц! 

Установка и настройка Клонируете репозиторий.

Вариант А:

Установите зависимости: pip install -r requirements.txt

Примените миграции: python manage.py migrate

Перейдите в раздел config/settings.py , найстройте там вашу бд

Создайте бд. Далее в файле 4 пункта, найдите раздел DATABASES, введите ваши данные


Создайте файл .env и пропишите все данные из .env.sample

Запустите сервер разработки: python manage.py runserver

в отдельных окнах терминала запускаете селери
celery -A config beat -l info -S django 

celery -A config worker -l INFO -P eventlet
