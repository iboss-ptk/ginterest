from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ginterest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/', views.current_datetime),
]
