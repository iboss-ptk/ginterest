# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150426_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtable',
            name='main_table',
            field=models.ForeignKey(to='app.DTable'),
        ),
    ]