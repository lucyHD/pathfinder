# Generated by Django 3.0.7 on 2020-06-25 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phenomena', '0003_auto_20200624_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='TESTname',
        ),
    ]
