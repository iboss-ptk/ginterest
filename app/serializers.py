# from django.contrib.auth.models import User, Group
from app.models import *
from rest_framework import serializers


class SystemRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemRole
        fields = ('id', 'role_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'role_id')


class DTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DTable
        fields = ('id', 'status', 'description', 'capacity', 'main_table')


class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = ('id', 'number_of_customer', 'queue_no', 'enter_time', 'exit_time')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'firstname', 'lastname', 'home_tel_no', 'mobile_no',
                  'number_of_seat', 'reserved_time', 'customer_id')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'price')


class OrderlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderlist
        fields = ('id', 'dtable_id', 'customergroup_id')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname', 'home_tel_no', 'mobile_no', 'pic_path', 'address', 'role')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_time', 'status', 'comment', 'quantity', 'menu_id', 'orderlist_id')


class SalariedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaried
        fields = ('id', 'employee_id', 'salary')


class HourlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hourly
        fields = ('id', 'employee_id', 'wage')


class WorktimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worktime
        fields = ('id', 'employee_id', 'day_of_week', 'start_time', 'end_time')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name')


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'invoice_status', 'date', 'supplier_id', 'status')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'menu_id', 'ingredient_id', 'quantity_used')


class SitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sit
        fields = ('id', 'table_id', 'customer_id')


class InInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InInvoice
        fields = ('id', 'ingredient_id', 'invoice_id', 'quantity_bought', 'price')