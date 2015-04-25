# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DTableModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(choices=[('u', 'InUsed'), ('o', 'Vacant'), ('r', 'Reserved')], max_length=1)),
                ('description', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(default=2)),
                ('main_table', models.ForeignKey(to='app.DTableModel')),
            ],
        ),
        migrations.CreateModel(
            name='SystemRoleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role_id', models.ForeignKey(to='app.SystemRoleModel')),
            ],
        ),
    ]
