# Generated by Django 4.2.6 on 2024-02-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_booking_client_alter_booking_guests_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='client',
        ),
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6 и более человек')], verbose_name='Количество гостей'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=15, unique=True, verbose_name='Номер телефона'),
        ),
    ]