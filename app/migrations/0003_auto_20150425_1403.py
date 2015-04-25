# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customergroupmodel_employeemodel_hourlymodel_ingredientmodel_menumodel_orderlistmodel_ordermodel_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='InInvoiceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_bought', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=1)),
                ('ingredient_id', models.ForeignKey(to='app.IngredientModel')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(max_length=1, choices=[('p', 'Pending'), ('o', 'Ordered'), ('d', 'Delivering'), ('f', 'Delivered')])),
            ],
        ),
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_used', models.IntegerField(default=1)),
                ('ingredient_id', models.ForeignKey(to='app.IngredientModel')),
                ('menu_id', models.ForeignKey(to='app.MenuModel')),
            ],
        ),
        migrations.CreateModel(
            name='SitModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.ForeignKey(to='app.CustomerGroupModel')),
                ('table_id', models.ForeignKey(to='app.DTableModel')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='WorktimeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_of_week', models.CharField(max_length=8)),
                ('start_time', models.CharField(max_length=5)),
                ('end_time', models.CharField(max_length=5)),
                ('employee_id', models.ForeignKey(to='app.EmployeeModel')),
            ],
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='supplier_id',
            field=models.ForeignKey(to='app.SupplierModel'),
        ),
        migrations.AddField(
            model_name='ininvoicemodel',
            name='invoice_id',
            field=models.ForeignKey(to='app.InvoiceModel'),
        ),
    ]
