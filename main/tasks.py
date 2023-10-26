from celery import shared_task
from django.utils import timezone
from main.models import Recipient
import requests, os
from dateutil.relativedelta import relativedelta


def send_sms(api_key, phone_number, message):
    url = "https://sms.ru/sms/send"
    payload = {
        "api_id": api_key,
        "to": phone_number,
        "msg": message,
        "json": 1  # Для получения ответа в формате JSON
    }
    response = requests.post(url, data=payload)
    result = response.json()
    return result



@shared_task
def check_reminds():
    """
    Функция проверки даты и времени для отправки уведомления
    """
    current_time = timezone.now().time()
    current_date = timezone.now().date()
    reminds_today = Recipient.objects.filter(
        send_date=current_date
    )
    print('we are here 1')
    for remind in reminds_today:
        print('we are here 2')
        if remind.send_time.hour <= current_time.hour and remind.send_time.minute <= current_time.minute:
            new_send_date = remind.send_date + relativedelta(months=1)    # Обновляем send_date у привычки
            remind.send_date = new_send_date
            remind.save()
            api_key = os.getenv('SMS_API')
            phone_number = remind.phone_number  # Номер получателя
            message = 'Здравствуйте! Сегодня день внесения данных по счетчикам!'
            result = send_sms(api_key, phone_number, message)
            print(result)  # Распечатайте ответ от API SMS.RU



