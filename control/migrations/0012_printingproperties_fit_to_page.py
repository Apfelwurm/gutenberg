# Generated by Django 4.0.4 on 2022-04-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0011_alter_jobartefact_artefact_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='printingproperties',
            name='fit_to_page',
            field=models.BooleanField(default=True),
        ),
    ]
