# Generated by Django 3.0.4 on 2020-05-06 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='image2',
        ),
    ]
