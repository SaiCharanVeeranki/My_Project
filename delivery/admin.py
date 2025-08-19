from django.contrib import admin
from .models import Customers, Restarunts, Menu, Cart

# Register your models here.
admin.site.register(Customers)
admin.site.register(Restarunts)
admin.site.register(Menu)
admin.site.register(Cart)