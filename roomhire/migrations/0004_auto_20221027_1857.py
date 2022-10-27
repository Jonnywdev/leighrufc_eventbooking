# Generated by Django 3.2 on 2022-10-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomhire', '0003_roomhire'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomhire',
            options={'verbose_name_plural': 'Room Hire Request'},
        ),
        migrations.AddField(
            model_name='roomhire',
            name='event_type',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='roomhire',
            name='date_of_event',
            field=models.DateField(),
        ),
    ]
