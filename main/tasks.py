from celery import shared_task
from django.utils import timezone
from main.models import Recipient
from dateutil.relativedelta import relativedelta


@shared_task
def check_habit():
    """
    Функция проверки даты и времени для отправки уведомления
    """
    current_time = timezone.now().time()
    current_date = timezone.now().date()
    recipients_today = Recipient.objects.filter(
        send_date=current_date
    )
    print('we are here 1')
    for recipient in recipients_today:
        print('we are here 2')
        if recipient.send_time.hour <= current_time.hour and recipient.send_time.minute <= current_time.minute:
            new_send_date = recipient.send_date + relativedelta(months=1)    # Обновляем send_date у привычки
            recipient.send_date = new_send_date
            recipient.save()

