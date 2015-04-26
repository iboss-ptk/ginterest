# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150425_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='customergroup_id',
            field=models.ForeignKey(default=None, to='app.CustomerGroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='exit_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='dtable',
            name='status',
            field=models.CharField(max_length=1, default='o', choices=[('u', 'InUsed'), ('o', 'Vacant'), ('r', 'Reserved')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pic_path',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='ininvoice',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(max_length=1, default='p', choices=[('p', 'Pending'), ('o', 'Ordered'), ('d', 'Delivering'), ('f', 'Delivered')]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pic_path',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=1, default='q', choices=[('q', 'Queuing'), ('c', 'Being cooked'), ('f', 'Finished')]),
        ),
    ]
