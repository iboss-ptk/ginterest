# Create your views here.


from django.http import HttpResponse
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
