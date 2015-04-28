# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150427_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='pic_path',
            field=models.ImageField(upload_to='pictures/', default='pictures/no-img.jpg'),
        ),
    ]
