# Generated by Django 4.0.4 on 2022-04-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0009_jobartefact'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobartefact',
            name='mime_type',
            field=models.CharField(default='application/octet-stream', max_length=100),
        ),
    ]
