# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150427_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFreakingFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='pic_path',
            field=models.ImageField(default='pictures/no-img.jpg', upload_to='employee_pic/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=1, choices=[('m', 'Manager'), ('c', 'Chef'), ('w', 'WaitingStaff'), ('s', 'Staff'), ('t', 'Trainee'), ('f', 'Fired')]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pic_path',
            field=models.ImageField(default='pictures/no-img.jpg', upload_to='menu_pic/'),
        ),
    ]
