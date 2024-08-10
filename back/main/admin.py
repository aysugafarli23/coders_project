from django.contrib import admin
from .models import Portfolio, Product, Agent, Service, ProductImage,Customer

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('product_name', 'product_price', 'product_location')

admin.site.register(Portfolio)
admin.site.register(Product, ProductAdmin)
admin.site.register(Agent)
admin.site.register(Service)
admin.site.register(Customer)
