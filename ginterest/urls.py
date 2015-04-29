from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
from f7 import views as f7_views
from rest_framework import routers

# api router
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'system_role', views.SystemRoleViewSet)
router.register(r'dtable', views.DTableViewSet)
router.register(r'customergroup', views.CustomerGroupViewSet)
router.register(r'reservation', views.ReservationViewSet)
router.register(r'menu', views.MenuViewSet)
router.register(r'orderlist', views.OrderlistViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'salaried', views.SalariedViewSet)
router.register(r'hourly', views.HourlyViewSet)
router.register(r'worktime', views.WorktimeViewSet)
router.register(r'ingredient', views.IngredientViewSet)
# router.register(r'supplier', views.SupplierViewSet)
# router.register(r'invoice', views.InvoiceViewSet)
router.register(r'recipe', views.RecipeViewSet)
router.register(r'sit', views.SitViewSet)
# router.register(r'invoice', views.InvoiceViewSet)
# router.register(r'ininvoice', views.InInvoiceViewSet)

urlpatterns = [
    # Examples:
    url(r'^$', f7_views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
