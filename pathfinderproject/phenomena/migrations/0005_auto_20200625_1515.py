# Generated by Django 3.0.7 on 2020-06-25 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phenomena', '0004_auto_20200625_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='TESTname',
            new_name='name',
        ),
    ]
