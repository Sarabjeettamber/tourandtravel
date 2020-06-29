# Generated by Django 3.0.4 on 2020-05-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paygate', '0008_auto_20200520_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotelbook',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('Adult', models.CharField(max_length=30)),
                ('Children', models.CharField(max_length=30)),
                ('ACRooms', models.CharField(max_length=30)),
                ('NonACRooms', models.CharField(max_length=30)),
            ],
        ),
    ]
