from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from materials.models import Course
from users.models import Subscription, User


@shared_task
def message_update_course(pk):
    """task for sending warning message about updates of course"""
    course = Course.objects.get(pk=pk)
    subs = Subscription.objects.filter(course=course)
    # send message only if last update of the course less than 4 hours
    if course.last_update + timedelta(hours=4) < timezone.now():
        course.last_update = timezone.now()
        for s in subs:
            # print(s.user)
            send_mail(
                subject=f'Курс {course.title} изменен',
                message=f'Посмотрите изменения на курсе {course.title}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[s.user]
            )
