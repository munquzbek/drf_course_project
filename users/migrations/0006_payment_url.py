# Generated by Django 5.0.4 on 2024-05-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='url',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Ссылка оплаты'),
        ),
    ]
