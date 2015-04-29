# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('number_of_customer', models.IntegerField(default=1)),
                ('queue_no', models.IntegerField(default=0)),
                ('enter_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DTable',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status', models.CharField(default='o', max_length=1, choices=[('u', 'InUsed'), ('o', 'Vacant'), ('r', 'Reserved'), ('c', 'Checking out')])),
                ('description', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(default=2)),
                ('main_table', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('home_tel_no', models.CharField(max_length=9)),
                ('mobile_no', models.CharField(max_length=10)),
                ('pic_path', models.ImageField(default='pictures/no-img.jpg', upload_to='employee_pic/')),
                ('address', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=1, choices=[('m', 'Manager'), ('c', 'Chef'), ('w', 'WaitingStaff'), ('s', 'Staff'), ('t', 'Trainee'), ('f', 'Fired')])),
            ],
        ),
        migrations.CreateModel(
            name='Hourly',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('wage', models.IntegerField(default=40)),
                ('employee_id', models.ForeignKey(to='app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='InInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity_bought', models.IntegerField(default=1)),
                ('price', models.FloatField(default=1)),
                ('ingredient_id', models.ForeignKey(to='app.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(default='p', max_length=1, choices=[('p', 'Pending'), ('o', 'Ordered'), ('d', 'Delivering'), ('f', 'Delivered')])),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('pic_path', models.ImageField(default='pictures/no-img.jpg', upload_to='menu_pic/')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='q', max_length=1, choices=[('q', 'Queuing'), ('c', 'Being cooked'), ('f', 'Finished cooking'), ('s', 'served')])),
                ('comment', models.CharField(max_length=70)),
                ('quantity', models.IntegerField(default=1)),
                ('menu_id', models.ForeignKey(to='app.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Orderlist',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('customergroup_id', models.ForeignKey(to='app.CustomerGroup')),
                ('dtable_id', models.ForeignKey(to='app.DTable')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity_used', models.IntegerField(default=1)),
                ('ingredient_id', models.ForeignKey(to='app.Ingredient')),
                ('menu_id', models.ForeignKey(to='app.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('home_tel_no', models.CharField(max_length=9)),
                ('mobile_no', models.CharField(max_length=10)),
                ('number_of_seat', models.IntegerField(default=1)),
                ('reserved_time', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(to='app.CustomerGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Salaried',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('salary', models.IntegerField(default=15000)),
                ('employee_id', models.ForeignKey(to='app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(to='app.CustomerGroup')),
                ('table_id', models.ForeignKey(to='app.DTable')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SystemRole',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role_id', models.ForeignKey(to='app.SystemRole')),
            ],
        ),
        migrations.CreateModel(
            name='Worktime',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=3, choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('employee_id', models.ForeignKey(to='app.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orderlist_id',
            field=models.ForeignKey(to='app.Orderlist'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier_id',
            field=models.ForeignKey(to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='ininvoice',
            name='invoice_id',
            field=models.ForeignKey(to='app.Invoice'),
        ),
        migrations.AddField(
            model_name='dtable',
            name='user_id',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
