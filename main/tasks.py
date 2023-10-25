from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from main.models import Recipient



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
    for remind in reminds_today:
        if remind.send_time.hour <= current_time.hour and remind.send_time.minute <= current_time.minute:
            #send_message_tg(habit.creator.telegram_username, habit.time, habit.place, habit.action)
            new_send_date = remind.send_date + timedelta(days=remind.periodicity)    # Обновляем send_date у привычки
            remind.send_date = new_send_date
            remind.save()