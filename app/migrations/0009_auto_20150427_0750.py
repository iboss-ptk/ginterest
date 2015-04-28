# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150426_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='employee_id',
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='exit_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dtable',
            name='main_table',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pic_path',
            field=models.ImageField(upload_to='menu_pic'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='q', max_length=1, choices=[('q', 'Queuing'), ('c', 'Being cooked'), ('f', 'Finished cooking'), ('s', 'served')]),
        ),
    ]
