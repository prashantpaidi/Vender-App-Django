# Generated by Django 3.2.5 on 2021-08-04 07:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tender', '0005_rename_bids_bid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bid',
            unique_together={('user', 'tender')},
        ),
    ]