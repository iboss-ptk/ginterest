# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150425_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hourly',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('wage', models.IntegerField(default=40)),
            ],
        ),
        migrations.CreateModel(
            name='InInvoice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('quantity_bought', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(max_length=1, choices=[('p', 'Pending'), ('o', 'Ordered'), ('d', 'Delivering'), ('f', 'Delivered')])),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('quantity_used', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Salaried',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(default=15000)),
            ],
        ),
        migrations.CreateModel(
            name='Worktime',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=3, choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='CustomerGroupModel',
            new_name='CustomerGroup',
        ),
        migrations.RenameModel(
            old_name='DTableModel',
            new_name='DTable',
        ),
        migrations.RenameModel(
            old_name='EmployeeModel',
            new_name='Employee',
        ),
        migrations.RenameModel(
            old_name='SupplierModel',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='MenuModel',
            new_name='Menu',
        ),
        migrations.RenameModel(
            old_name='OrderModel',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrderlistModel',
            new_name='Orderlist',
        ),
        migrations.RenameModel(
            old_name='ReservationModel',
            new_name='Reservation',
        ),
        migrations.RenameModel(
            old_name='SitModel',
            new_name='Sit',
        ),
        migrations.RenameModel(
            old_name='IngredientModel',
            new_name='Supplier',
        ),
        migrations.RenameModel(
            old_name='SystemRoleModel',
            new_name='SystemRole',
        ),
        migrations.RenameModel(
            old_name='UserModel',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='hourlymodel',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='ininvoicemodel',
            name='ingredient_id',
        ),
        migrations.RemoveField(
            model_name='ininvoicemodel',
            name='invoice_id',
        ),
        migrations.RemoveField(
            model_name='invoicemodel',
            name='supplier_id',
        ),
        migrations.RemoveField(
            model_name='recipemodel',
            name='ingredient_id',
        ),
        migrations.RemoveField(
            model_name='recipemodel',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='salariedmodel',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='worktimemodel',
            name='employee_id',
        ),
        migrations.DeleteModel(
            name='HourlyModel',
        ),
        migrations.DeleteModel(
            name='InInvoiceModel',
        ),
        migrations.DeleteModel(
            name='InvoiceModel',
        ),
        migrations.DeleteModel(
            name='RecipeModel',
        ),
        migrations.DeleteModel(
            name='SalariedModel',
        ),
        migrations.DeleteModel(
            name='WorktimeModel',
        ),
        migrations.AddField(
            model_name='worktime',
            name='employee_id',
            field=models.ForeignKey(to='app.Employee'),
        ),
        migrations.AddField(
            model_name='salaried',
            name='employee_id',
            field=models.ForeignKey(to='app.Employee'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient_id',
            field=models.ForeignKey(to='app.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='menu_id',
            field=models.ForeignKey(to='app.Menu'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier_id',
            field=models.ForeignKey(to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='ininvoice',
            name='ingredient_id',
            field=models.ForeignKey(to='app.Ingredient'),
        ),
        migrations.AddField(
            model_name='ininvoice',
            name='invoice_id',
            field=models.ForeignKey(to='app.Invoice'),
        ),
        migrations.AddField(
            model_name='hourly',
            name='employee_id',
            field=models.ForeignKey(to='app.Employee'),
        ),
    ]
