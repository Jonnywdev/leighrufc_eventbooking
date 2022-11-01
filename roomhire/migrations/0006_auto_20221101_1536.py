# Generated by Django 3.2 on 2022-11-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomhire', '0005_alter_roomhire_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomhire',
            name='entertainer',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomhire',
            name='kitchen',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomhire',
            name='member',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomhire',
            name='room_dressed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]