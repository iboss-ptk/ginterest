from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from app.models import *
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

    @list_route(methods=['post'])
    def login(self, request):
        """
        Authenticate the user and store session
        """
        data = request.DATA
        resp = User.authenticate(data['username'], data['password'])

        if resp['isAuthenticated']:
            # TODO: need get_table_id. none if not table
            # if User.objects.get(pk=resp.id) =
            request.session['user_id'] = resp.id
            request.session['role_id'] = resp.role_id
        return Response(resp)


class DTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DTable to be viewed or edited.
    """
    queryset = DTable.objects.all()
    serializer_class = DTableSerializer

    @detail_route()
    def wait_for_activation(self, request, pk=None):
        resp = {'status': self.get_object().status}
        return Response(resp)

    @list_route()
    def get_all_menu(self, request):
        menu_list = Menu.get_all_menu()
        resp = {'menu_list': menu_list}
        return Response(resp)

    @list_route(methods=['post'])
    def activate_table(self, request):
        is_successful = DTable.activate_table(request.DATA['dtable_id'], request.DATA['customergroup_id'])
        resp = {'is_successful': is_successful}
        return Response(resp)



class CustomerGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CustomerGroup to be viewed or edited.
    """
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer

    @detail_route(methods=['post'])
    def add_order_to_orderlist(self, request, pk=None):
        comment = ''
        if 'comment' in request.DATA:
            comment = request.DATA['comment']
        menu_id, quantity = request.DATA['menu_id'], request.DATA['quantity']
        resp = {'isSuccessful': self.get_object().add_to_orderlist(menu_id, quantity, comment)}
        return Response(resp)

    @detail_route()
    def get_order_list(self, request, pk=None):
        order_list = self.get_object().get_order_list()
        resp = {'order_list': order_list}
        return Response(resp)

    @detail_route()
    def checkout(self, request):
        resp = {"a": 123}
        return Response(resp)



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


# class SupplierViewSet (viewsets.ModelViewSet):
#     """
#     API endpoint that allows Supplier to be viewed or edited.
#     """
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer


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


# class InvoiceViewSet (viewsets.ModelViewSet):
#     """
#     API endpoint that allows Invoice to be viewed or edited.
#     """
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer


# class InInvoiceViewSet (viewsets.ModelViewSet):
#     """
#     API endpoint that allows InInvoice to be viewed or edited.
#     """
#     queryset = InInvoice.objects.all()
#     serializer_class = InInvoiceSerializer
