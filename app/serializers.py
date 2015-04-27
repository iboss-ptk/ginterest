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
