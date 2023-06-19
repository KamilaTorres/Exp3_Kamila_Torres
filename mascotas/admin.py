from django.contrib import admin
from .models import Producto
from django.contrib.admin import AdminSite
from django.urls import reverse_lazy,path
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.register(Producto)


