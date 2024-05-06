from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')

    country = models.CharField(verbose_name='страна',
                               **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []


class Payment(models.Model):
    TYPE_PAYMENT = [('CASH', 'Наличка'), ('CARD', 'Оплата картой')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ползователь', related_name='payment',
                             **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс',
                               related_name='paid_course', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок',
                               related_name='paid_lesson', **NULLABLE)
    payment_date = models.DateField(verbose_name='дата оплаты')
    amount_pay = models.PositiveIntegerField(verbose_name='сумма оплаты')
    type_payment = models.CharField(max_length=50, verbose_name='способ оплаты', choices=TYPE_PAYMENT)

    def __str__(self):
        return f'{self.amount_pay}$, for {self.course if self.course else self.lesson}, {self.user}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ('-payment_date',)
