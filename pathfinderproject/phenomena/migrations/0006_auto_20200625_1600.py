# Generated by Django 3.0.7 on 2020-06-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenomena', '0005_auto_20200625_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]