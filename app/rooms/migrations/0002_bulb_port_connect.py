# Generated by Django 2.1.1 on 2018-09-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulb',
            name='port_connect',
            field=models.IntegerField(default=0),
        ),
    ]