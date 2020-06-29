# Generated by Django 3.0.4 on 2020-06-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0014_popular'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidayspackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagename', models.CharField(max_length=40)),
                ('suitablegroup', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='pics')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
                ('image1', models.ImageField(null=True, upload_to='pics')),
                ('name1', models.CharField(max_length=40, null=True)),
                ('lengthofstay1', models.IntegerField(null=True)),
                ('description1', models.CharField(max_length=20000, null=True)),
                ('location1', models.CharField(max_length=200, null=True)),
                ('image2', models.ImageField(null=True, upload_to='pics')),
                ('name2', models.CharField(max_length=40, null=True)),
                ('lengthofstay2', models.IntegerField(null=True)),
                ('description2', models.CharField(max_length=20000, null=True)),
                ('location2', models.CharField(max_length=200, null=True)),
                ('image3', models.ImageField(null=True, upload_to='pics')),
                ('name3', models.CharField(max_length=40, null=True)),
                ('lengthofstay3', models.IntegerField(null=True)),
                ('description3', models.CharField(max_length=20000, null=True)),
                ('location3', models.CharField(max_length=200, null=True)),
                ('image4', models.ImageField(null=True, upload_to='pics')),
                ('name4', models.CharField(max_length=40, null=True)),
                ('lengthofstay4', models.IntegerField(null=True)),
                ('description4', models.CharField(max_length=20000, null=True)),
                ('location4', models.CharField(max_length=200, null=True)),
                ('image5', models.ImageField(null=True, upload_to='pics')),
                ('name5', models.CharField(max_length=40, null=True)),
                ('lengthofstay5', models.IntegerField(null=True)),
                ('description5', models.CharField(max_length=20000, null=True)),
                ('location5', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]