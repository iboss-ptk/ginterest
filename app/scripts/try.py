from app.models import *

def run():
    c1 = CustomerGroup.objects.get(pk=1)
    ol1 = Orderlist.objects.get(pk=1)
    o1 = Order.objects.get(pk=1)
    m1 = Menu.objects.get(pk=1)
    e1 = Employee.objects.get(pk=1)

    print(e1.is_chef()) # True
    print(e1.fire())    # FIRED!
    print(e1.role)      # f

    # print(AllFreakingFunction.total_income(c1))
    # The above function is still broken because of total_income function in Models
    # The error is "AttributeError: 'Orderlist' object has no attribute 'split' "