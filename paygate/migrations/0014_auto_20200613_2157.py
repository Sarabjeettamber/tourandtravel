# Generated by Django 3.0.4 on 2020-06-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paygate', '0013_auto_20200612_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbook',
            name='ACRooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hotelbook',
            name='Adult',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hotelbook',
            name='Children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hotelbook',
            name='NonACRooms',
            field=models.IntegerField(),
        ),
    ]
