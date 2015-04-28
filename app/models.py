from django.db import models
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


class DTable(models.Model):
    TABLE_STATUSES = (
        ('u', 'InUsed'),
        ('o', 'Vacant'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=TABLE_STATUSES, default='o')
    description = models.CharField(max_length=200)
    capacity = models.IntegerField(default=2)
    main_table = models.IntegerField(default=-1)

    def __str__(self):
        return str(self.id)+' '+self.description


class CustomerGroup(models.Model):
    number_of_customer = models.IntegerField(default=1)
    queue_no = models.IntegerField(default=0)
    enter_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now_add=True)

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
        return Order.objects.prefetch_related(Order.menu_id).filter(orderlist_id=self.get_order_list())



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


# for testing
class AllFreakingFunction(models.Model):
    def total_income(cg):
        total = 0
        orderL = Orderlist.objects.get(customergroup_id=cg)
        allOrders = Order.objects.all().prefetch_related(orderL)
        for order in allOrders:
                morder = Menu.objects.all().prefetch_releated(order)
                total+= (order.quantity)*(morder.price)
        return total
