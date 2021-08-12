# Generated by Django 3.2.5 on 2021-08-08 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0010_auto_20210808_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderwinner',
            name='tender',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tender.tender', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='tenderwinner',
            unique_together=set(),
        ),
    ]
