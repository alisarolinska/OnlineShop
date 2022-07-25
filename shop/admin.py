from django.contrib import admin

from shop.models import Product, Comment


admin.site.register(Product)
admin.site.register(Comment)

"""
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'desription', 'price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at' ]
    list_editable = ['price', 'description' ]
    prepopulated_fields = ['id']


admin.site.register(ProductAdmin)
"""
