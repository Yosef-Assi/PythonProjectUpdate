# Generated by Django 2.2.4 on 2022-10-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='violaion',
            name='expierd_date',
            field=models.DateField(null=True),
        ),
    ]
