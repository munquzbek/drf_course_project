from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def deactivate_users():
    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login:
            if timezone.now().date() - user.last_login.date() > timedelta(days=30):
                user.is_active = False
                user.save()

