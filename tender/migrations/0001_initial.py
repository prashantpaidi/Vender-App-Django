# Generated by Django 3.2.5 on 2021-07-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tendname', models.CharField(max_length=100)),
                ('tenddesc', models.CharField(max_length=500)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
    ]
