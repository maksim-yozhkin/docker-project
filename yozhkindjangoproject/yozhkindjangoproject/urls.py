from django.contrib import admin
from django.urls import path
from djangoapp.views import data_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_table),
]
