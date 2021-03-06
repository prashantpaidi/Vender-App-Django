# Generated by Django 3.2.5 on 2021-08-08 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tender', '0012_auto_20210808_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderwinner',
            name='tender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tender.tender', unique=True),
        ),
        migrations.AlterField(
            model_name='tenderwinner',
            name='user',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
