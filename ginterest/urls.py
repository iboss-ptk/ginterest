from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'system_role', views.SystemRoleViewSet)
router.register(r'dtable', views.DTableViewSet)
router.register(r'customergroup', views.CustomerGroupViewSet)
router.register(r'reservation', views.ReservationViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'ginterest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
