from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('Check', views.Check,name="Check"),
]
