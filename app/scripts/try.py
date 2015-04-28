from app.models import *

def run():
    c1 = CustomerGroup.objects.get(pk=1)
    ol1 = Orderlist.objects.get(pk=1)
    o1 = Order.objects.get(pk=1)
    m1 = Menu.objects.get(pk=1)
    e1 = Employee.objects.get(pk=1)


    # test authenticate
    # print(User.authenticate('janin', 'jap')) #correct username, password
    # print(User.authenticate('janin', 'kuy')) #wrong password
    # print(User.authenticate('janinuy', 'jap')) #wrong username
    # print(User.authenticate('janinuy', 'kuy')) #wrong username, password

    # print(DTable.objects.get(pk=1).status)
    # print(Reservation.activate_table(1,1))

    # print(Reservation.activate_table(1,1))

    # c1.add_to_orderlist(m1, 1, "-")

    # for m_order in c1.get_order_list():
    #     print(m_order)

    # print(e1.is_chef()) # True
    # print(e1.fire())    # FIRED!
    # print(e1.role)      # f

    # print(AllFreakingFunction.total_income(c1))
    # The above function is still broken because of total_income function in Models
    # The error is "AttributeError: 'Orderlist' object has no attribute 'split' "