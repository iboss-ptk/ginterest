from rest_framework import viewsets
from app.serializers import *


class SystemRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SystemRole to be viewed or edited.
    """
    queryset = SystemRole.objects.all()
    serializer_class = SystemRoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DTable to be viewed or edited.
    """
    queryset = DTable.objects.all()
    serializer_class = DTableSerializer


class CustomerGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CustomerGroup to be viewed or edited.
    """
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Reservation to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderlistViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows OrderList to be viewed or edited.
    """
    queryset = Orderlist.objects.all()
    serializer_class = OrderlistSerializer


class EmployeeViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Employee to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class OrderViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Order to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SalariedViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Salaried to be viewed or edited.
    """
    queryset = Salaried.objects.all()
    serializer_class = SalariedSerializer


class HourlyViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Hourly to be viewed or edited.
    """
    queryset = Hourly.objects.all()
    serializer_class = HourlySerializer


class WorktimeViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Worktime to be viewed or edited.
    """
    queryset = Worktime.objects.all()
    serializer_class = WorktimeSerializer


class IngredientViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredient to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class SupplierViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Supplier to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class RecipeViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Recipe to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class SitViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Sit to be viewed or edited.
    """
    queryset = Sit.objects.all()
    serializer_class = SitSerializer


class InvoiceViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows Invoice to be viewed or edited.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InInvoiceViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows InInvoice to be viewed or edited.
    """
    queryset = InInvoice.objects.all()
    serializer_class = InInvoiceSerializer