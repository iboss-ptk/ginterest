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
    d1 = DTable(description='aiiaor')
    d2 = DTable(description='iboss')
    d3 = DTable(description='ong')
    d4 = DTable(description='janin')
    d5 = DTable(description='fony')
    d6 = DTable(description='pete')
    d1.save()
    d2.save()
    d3.save()
    d4.save()
    d5.save()
    d6.save()

    # CustomerGroup,
    cg1= CustomerGroup(number_of_customer=3)
    cg2= CustomerGroup(number_of_customer=2)
    cg3= CustomerGroup(number_of_customer=5)
    cg4= CustomerGroup(number_of_customer=1)
    cg5= CustomerGroup(number_of_customer=4)
    cg6= CustomerGroup(number_of_customer=2)
    cg1.save()
    cg2.save()
    cg3.save()
    cg4.save()
    cg5.save()
    cg6.save()

    # Reservation,
    r1 = Reservation(firstname='janin',lastname='jap',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg1)
    r2 = Reservation(firstname='aiiaor',lastname='boon',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg2)
    r3 = Reservation(firstname='iboss',lastname='ibosza',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg3)
    r4 = Reservation(firstname='fony',lastname='laew',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg4)
    r5 = Reservation(firstname='ong',lastname='patinya',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg5)
    r6 = Reservation(firstname='aekamon',lastname='pete',home_tel_no='012345678',mobile_no='0123456789',customer_id=cg6)
    r1.save()
    r2.save()
    r3.save()
    r4.save()
    r5.save()
    r6.save()


    # Menu,
   # m1=Menu(name='janin',description='jap',pic_path)
    # Orderlist,
    # Employee,
    # Order,
    # Salaried,
    # Hourly,
    # Worktime,
    # Ingredient,
    # Supplier,
    # Invoice,
    # Recipe,
    # Sit,
    # InInvoice

