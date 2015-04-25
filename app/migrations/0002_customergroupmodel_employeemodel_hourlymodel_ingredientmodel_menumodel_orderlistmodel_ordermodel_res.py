# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGroupModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number_of_customer', models.IntegerField(default=1)),
                ('queue_no', models.IntegerField(default=0)),
                ('enter_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('home_tel_no', models.CharField(max_length=9)),
                ('mobile_no', models.CharField(max_length=10)),
                ('pic_path', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('m', 'Manager'), ('c', 'Chef'), ('w', 'WaitingStaff'), ('s', 'Staff'), ('t', 'Trainee')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='HourlyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('wage', models.IntegerField(default=40)),
                ('employee_id', models.ForeignKey(to='app.EmployeeModel')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('pic_path', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderlistModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('dtable_id', models.ForeignKey(to='app.DTableModel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('q', 'Queuing'), ('c', 'Being cooked'), ('f', 'Finished')], max_length=1)),
                ('comment', models.CharField(max_length=70)),
                ('quantity', models.IntegerField(default=1)),
                ('employee_id', models.ForeignKey(to='app.EmployeeModel')),
                ('menu_id', models.ForeignKey(to='app.MenuModel')),
                ('orderlist_id', models.ForeignKey(to='app.OrderlistModel')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('home_tel_no', models.CharField(max_length=9)),
                ('mobile_no', models.CharField(max_length=10)),
                ('number_of_seat', models.IntegerField(default=1)),
                ('reserved_time', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(to='app.CustomerGroupModel')),
            ],
        ),
        migrations.CreateModel(
            name='SalariedModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('salary', models.IntegerField(default=15000)),
                ('employee_id', models.ForeignKey(to='app.EmployeeModel')),
            ],
        ),
    ]
