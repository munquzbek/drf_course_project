# Generated by Django 5.0.4 on 2024-05-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_payment_course_alter_payment_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, null=True, verbose_name='страна'),
        ),
    ]
