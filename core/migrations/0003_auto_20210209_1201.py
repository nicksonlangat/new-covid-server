# Generated by Django 3.1.6 on 2021-02-09 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_appointment_appointment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 12, 1, 14, 684623)),
            preserve_default=False,
        ),
    ]
