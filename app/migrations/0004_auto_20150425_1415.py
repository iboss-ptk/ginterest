# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150425_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktimemodel',
            name='day_of_week',
            field=models.CharField(max_length=3, choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')]),
        ),
        migrations.AlterField(
            model_name='worktimemodel',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='worktimemodel',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
