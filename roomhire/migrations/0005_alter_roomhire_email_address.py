# Generated by Django 3.2 on 2022-10-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomhire', '0004_auto_20221027_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomhire',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
