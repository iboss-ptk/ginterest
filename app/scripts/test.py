import django
django.setup()
from app.models import SystemRole,User,DTable,CustomerGroup,Reservation,Menu,Orderlist,Employee,Order,Salaried,Hourly,Worktime,Ingredient,Supplier,Invoice,Recipe,Sit,InInvoice
from django.utils import timezone

def run():
    #SystemRole
    s1 = SystemRole(role_name = 'TableScreen')
    s2 = SystemRole(role_name = 'ReceptionScreen')
    s3 = SystemRole(role_name = 'ServeScreen')
    s4 = SystemRole(role_name = 'ChefScreen')
    s5 = SystemRole(role_name = 'StockScreen')
    s6 = SystemRole(role_name = 'ManagerDashboard')
    s1.save()
    s2.save()
    s3.save()
    s4.save()
    s5.save()
    s6.save()
    all_sysrole = SystemRole.objects.all()

    #User,
    u1 = User(username ='janin',password='jap',role_id=s1)
    u2 = User(username ='fony',password='fony',role_id=s2)
    u3 = User(username ='aiiaor',password='aiiaor',role_id=s3)
    u4 = User(username ='ong',password='ong',role_id=s4)
    u5 = User(username ='eakamon',password='eakamon',role_id=s5)
    u6 = User(username ='iboss',password='iboss',role_id=s6)
    u1.save()
    u2.save()
    u3.save()
    u4.save()
    u5.save()
    u6.save()
    all_user = User.objects.all()

    #DTable,




    # CustomerGroup,
    # Reservation,
    # Menu,Orderlist,
    # Employee,Order,
    # Salaried,
    # Hourly,
    # Worktime,
    # Ingredient,
    # Supplier,
    # Invoice,
    # Recipe,
    # Sit,
    # InInvoice

