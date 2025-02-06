import time
from celery import shared_task
from django.core.mail import send_mail
from config import settings


@shared_task
def send_mail_task(recipient, subject, body):
    """Задача отправки СМС"""
    # time.sleep(10)
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
    )
    return f'Email sent to {recipient}'



@shared_task
def add_product_task_log(product_name,):
    """Задача для логированя при добавлении продукта """
    creat_time = time.ctime(time.time())
    with open("log.txt", "a") as file:
        file.write(f'{creat_time} создан товар {product_name} \n')
    print(f'Товар {product_name} создан в {creat_time}')
    return f'Товар {product_name} создан'
