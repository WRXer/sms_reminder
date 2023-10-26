celery -A config beat -l info -S django 
celery -A config worker -l INFO -P eventlet
# sms_reminder
