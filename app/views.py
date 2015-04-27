# Create your views here.


from django.http import HttpResponse
from rest_framework import viewsets
from app.serializers import *


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer