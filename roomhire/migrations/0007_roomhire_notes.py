# Generated by Django 3.2 on 2022-11-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomhire', '0006_auto_20221101_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomhire',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]