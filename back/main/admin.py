from django.contrib import admin
from .models import Portfolio,Product,Agent,Service
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Product)
admin.site.register(Agent)
admin.site.register(Service)