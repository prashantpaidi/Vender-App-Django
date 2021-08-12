# Generated by Django 3.2.5 on 2021-08-10 05:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0014_alter_tenderwinner_tender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='start_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
