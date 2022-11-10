import os

from celery import shared_task
from django.core.mail import send_mail

from users.models import User


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_emails():
    users = User.objects.all()
    for i in users:
        send_mail('your account statictics', f'Username:{i.username} curent balance:{i.current_balance}',
                  os.environ.get("EMAIL_HOST_USER")[i.email],
                  fail_silently=False)
