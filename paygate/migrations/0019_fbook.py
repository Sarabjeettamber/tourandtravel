# Generated by Django 3.0.4 on 2020-06-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paygate', '0018_auto_20200629_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='fbook',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('packagename', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
    ]
