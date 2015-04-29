from django.db import models
import datetime
# Create your models here.


class SystemRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role_id = models.ForeignKey(SystemRole)

    def __str__(self):
        return self.username

    @staticmethod
    def authenticate(username, password):
        if User.objects.filter(username=username, password=password).exists():
            m_user = User.objects.get(username=username)
            return {'isAuthenticated': True,
                    'username': m_user.username,
                    'role_id': m_user.role_id.id}
        return {'isAuthenticated': False}

    def get_table_id(self):
        if self.role_id == 1:
            table_obj = DTable.objects.all().filter(user_id=self.id)
            return table_obj.id
        else:
            return None

    @staticmethod
    def is_table_vacant(table_id):
        table = DTable.objects.get(pk=table_id)
        if table.status == 'o':
            return True
        return False


class DTable(models.Model):
    TABLE_STATUSES = (
        ('u', 'InUsed'),
        ('o', 'Vacant'),
        ('r', 'Reserved'),
        ('c', 'Checking out'),
    )
    status = models.CharField(max_length=1, choices=TABLE_STATUSES, default='o')
    description = models.CharField(max_length=200)
    capacity = models.IntegerField(default=2)
    main_table = models.IntegerField(default=-1)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.id)+' '+self.description


class CustomerGroup(models.Model):
    number_of_customer = models.IntegerField(default=1)
    queue_no = models.IntegerField(default=0)
    enter_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now_add=True)
    exist = models.BooleanField(default=True)

    def __str__(self):
        return str(self.enter_time)+' ('+str(self.number_of_customer)+')'

    def add_to_orderlist(self, menuId, quantity, comment):
        mOrderlist = Orderlist.objects.get(customergroup_id=self)
        new_order = Order.objects.create(
            status='q', comment=comment,
            quantity=quantity, menu_id=menuId,
            orderlist_id=mOrderlist)
        new_order.save()
        return True

    def get_orderlist(self):
        return Orderlist.objects.get(customergroup_id=self)

    def get_order_list(self):
        order_list = []
        got_orders = Order.objects.all().filter(orderlist_id=self.get_orderlist())
        for order in got_orders:
            order_obj = {
                'name': order.menu_id.name,
                'quantity': order.quantity,
                'status': order.status,
                'price': order.menu_id.price
            }
            order_list.append(order_obj)
        return order_list


    def call_next_queue(old_queue_number):
        new_queue_number = old_queue_number
        last_customergroup = CustomerGroup.objects.order_by('queue_no').last()
        max_queue = last_customergroup.id
        if old_queue_number == max_queue:
            return max_queue

        while True:
            new_queue_number += 1
            if CustomerGroup.objects.filter(id=new_queue_number).exists():
                return new_queue_number
            if new_queue_number >= max_queue:
                return max_queue
        return -1

    @staticmethod
    def checkedout(customergroup_id):
        m_customergroup = CustomerGroup.objects.get(pk=customergroup_id)
        m_customergroup.exit_time = datetime.datetime.now()
        m_customergroup.save()

        m_table = Sit.get_table_of_customergroup(customergroup_id)
        m_table.status = 'o'
        m_table.save()

        return

    @staticmethod
    def initiate_queue():
        return CustomerGroup.objects.all().last().id


class Reservation(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    home_tel_no = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=10)
    number_of_seat = models.IntegerField(default=1)
    reserved_time = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return self.firstname+" "+str(self.reserved_time)

    @staticmethod
    def activate_table(table_id, customergroup_id):
        m_orderlist = Orderlist.create_new_orderlist(table_id, customergroup_id)
        m_table = DTable.objects.get(pk=table_id)
        if m_table.status == 'u' or m_table.status == 'r':
            return False

        new_sit = Sit.objects.create(
            table_id=DTable.objects.get(pk=table_id),
            customer_id=CustomerGroup.objects.get(pk=customergroup_id))
        m_table.status = 'u'

        m_table.save()
        m_orderlist.save()
        new_sit.save()

        return True


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    pic_path = models.ImageField(upload_to='menu_pic/', default='pictures/no-img.jpg')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Orderlist(models.Model):
    dtable_id = models.ForeignKey(DTable)
    customergroup_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return str(self.dtable_id)

    def total_price(self):
        price = 0
        orders = Order.objects.all().filter(orderlist_id=self)
        for order in orders:
            price += order.menu_id.price
        return price

    @staticmethod
    def create_new_orderlist(table_id, customergroup_id):
        new_orderlist = Orderlist.objects.create(
            dtable_id=DTable.objects.get(pk=table_id),
            customergroup_id=CustomerGroup.objects.get(pk=customergroup_id)
        )
        new_orderlist.save()
        return new_orderlist

    @staticmethod
    def get_all_checking_out_orderlist_list():
        orderlist_list = []
        orderlists = Orderlist.object.all().prefetch_related('dtable_id').filter(status='c')
        for orderlist in orderlists:
            orderlist_list.append({
                'dtable_id': orderlist.dtable_id.id,
                'total_price': orderlist.total_price()
            })
        return orderlist_list

    @staticmethod
    def get_checkingout_orderlist(dtable_id):
        order_list = []
        orderlist = Orderlist.objects.all().get(dtable_id=dtable_id).last()
        orders = Order.objects.all().filter(orderlist_id=orderlist)
        for order in orders:
            order_list.append({
                'menu_name': order.menu_id.name,
                'quantity': order.quantity,
                'price': order.menu_id.price
            })
        return order_list


class Employee(models.Model):
    CHEF = 'c'
    EMPLOYEE_ROLES = (
        ('m', 'Manager'),
        (CHEF, 'Chef'),
        ('w', 'WaitingStaff'),
        ('s', 'Staff'),
        ('t', 'Trainee'),
        ('f', 'Fired'),
    )
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    home_tel_no = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=10)
    pic_path = models.ImageField(upload_to='employee_pic/', default='pictures/no-img.jpg')
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=EMPLOYEE_ROLES)

    def __str__(self):
        return self.firstname+" "+self.lastname+" ["+self.role+"]"

    def is_chef(self):
        return self.role in self.CHEF

    def fire(self):
        self.role = 'f'
        return 'FIRED!'

    @staticmethod
    def total_income():
        income = 0
        leftcustomer = CustomerGroup.objects.all().filter(exist=False)
        orderlists = Orderlist.objects.all().filter(customergroup_id=leftcustomer)
        for orderlist in orderlists:
            orders = Order.objects.all().filter(orderlist_id=orderlist)
            for order in orders:
                income += order.menu_id.price
        return income


class Order(models.Model):
    ORDER_STATUSES = (
        ('q', 'Queuing'),
        ('c', 'Being cooked'),
        ('f', 'Finished cooking'),
        ('s', 'served'),
    )
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUSES, default='q')
    comment = models.CharField(max_length=70)
    quantity = models.IntegerField(default=1)
    menu_id = models.ForeignKey(Menu)
    orderlist_id = models.ForeignKey(Orderlist)

    def __str__(self):
        return str(self.menu_id.name)+" ("+str(self.quantity)+")"

    @staticmethod
    def get_unserved_order_list():
        m_order_list = Order.objects.all().prefetch_related('menu_id').filter(status='f')
        unserved_order_list = []
        for order in m_order_list:
            unserved_order_list.append({
                'order_id': order.id,
                'menu_name': order.menu_id.name,
                'menu_pic_path': order.menu_id.pic_path,
                'table_id': order.orderlist_id.dtable_id.id,
                'order_comment': order.comment,
                'order_quantity': order.quantity
            })
        return unserved_order_list

    @staticmethod
    def serve_order(order_id):
        if not Order.objects.get(pk=order_id, status='f').exist():
            return False
        m_order = Order.objects.get(pk=order_id)
        m_order.status = 's'
        m_order.save()
        return True

    @staticmethod
    def all_order_list():
        return_list = []
        m_all_order = Order.objects.prefetch_related('menu_id').all()
        for order in m_all_order:
            return_list.append({
                'menu_name': order.menu_id.name,
                'table_id': order.orderlist_id.dtable_id,
                'ordertime': order.order_time,
                'price': order.price
            })


class Salaried(models.Model):
    employee_id = models.ForeignKey(Employee)
    salary = models.IntegerField(default=15000)

    def __str__(self):
        return str(self.employee_id)+' @'+str(self.salary)


class Hourly(models.Model):
    employee_id = models.ForeignKey(Employee)
    wage = models.IntegerField(default=40)

    def __str__(self):
        return str(self.employee_id)+' @'+str(self.wage)


class Worktime(models.Model):
    DAYS_OF_WEEK = (
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
    )
    employee_id = models.ForeignKey(Employee)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.employee_id)+' - '+self.day_of_week+' @'+str(self.start_time)+' - '+str(self.end_time)


class Ingredient(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    menu_id = models.ForeignKey(Menu)
    ingredient_id = models.ForeignKey(Ingredient)
    quantity_used = models.IntegerField(default=1)

    def __str__(self):
        return str(self.quantity_used)+"x"+str(self.ingredient_id)+" @"+str(self.menu_id)


class Sit(models.Model):
    table_id = models.ForeignKey(DTable)
    customer_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return str(self.customer_id)+" @"+str(self.table_id)

    @staticmethod
    def get_sitting_customergroup(table_id):
        m_sit = Sit.objects.filter(
            table_id=DTable.objects.get(pk=table_id)).last()
        return m_sit.customer_id

    @staticmethod
    def get_table_of_customergroup(customergroup_id):
        m_sit = Sit.objects.filter(
            customer_id=CustomerGroup.objects.get(pk=customergroup_id)).last()
        return m_sit.table_id


class Invoice(models.Model):
    INVOICE_STATUSES = (
        ('p', 'Pending'),
        ('o', 'Ordered'),
        ('d', 'Delivering'),
        ('f', 'Delivered'),
    )
    date = models.DateTimeField('date published')
    supplier_id = models.ForeignKey(Supplier)
    status = models.CharField(max_length=1, choices=INVOICE_STATUSES, default='p')

    def __str__(self):
        return str(self.supplier_id)+" @"+str(self.date)

    def invoice_approve(self):
        self.status = 'o'
        return True


class InInvoice(models.Model):
    ingredient_id = models.ForeignKey(Ingredient)
    invoice_id = models.ForeignKey(Invoice)
    quantity_bought = models.IntegerField(default=1)
    price = models.FloatField(default=1)

    def __str__(self):
        return str(self.ingredient_id)+"x"+str(self.quantity_bought)+" @"+str(self.invoice_id)+" $"+str(self.price)
