# Generated by Django 3.0.4 on 2020-05-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20200518_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description2',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='description3',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='description4',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='description5',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='image2',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image3',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image4',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image5',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='package',
            name='lengthofstay2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='lengthofstay3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='lengthofstay4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='lengthofstay5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='location1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='location2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='location3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='location4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='location5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name4',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name5',
            field=models.CharField(max_length=40, null=True),
        ),
    ]