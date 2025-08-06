from django.contrib import admin
from .models import Customers, Restarunts, Menu

# Register your models here.
admin.site.register(Customers)
admin.site.register(Restarunts)
admin.site.register(Menu)