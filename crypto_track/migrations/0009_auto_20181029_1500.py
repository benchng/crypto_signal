# Generated by Django 2.1.2 on 2018-10-29 14:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_track', '0008_auto_20181026_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocandle',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 0, 29, 927794, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cryptocandlehistory',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 0, 29, 928570, tzinfo=utc)),
        ),
    ]