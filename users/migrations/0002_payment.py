# Generated by Django 5.0.4 on 2024-04-22 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='дата оплаты')),
                ('amount_pay', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('type_payment', models.CharField(choices=[('CASH', 'Наличка'), ('CARD', 'Оплата картой')], max_length=50, verbose_name='способ оплаты')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_course', to='materials.course', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_lesson', to='materials.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='ползователь')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
                'ordering': ('-payment_date',),
            },
        ),
    ]
