# Generated by Django 3.0.6 on 2020-05-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
