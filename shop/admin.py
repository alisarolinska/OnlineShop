from django.contrib import admin

from shop.models import Product, Comment, Category, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
#admin.site.register(Cart)
