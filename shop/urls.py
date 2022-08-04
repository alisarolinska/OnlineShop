from django.urls import path

from shop import views

urlpatterns = [
    path('orders/<int:product_id>', views.order_create, name='order_create'),
    path('category/<int:category>', views.get_products_by_category, name='category'),
    path('detail/<int:id>', views.product_detail_view, name='product-detail')
	# path('путь', views.функция, имя_запроса)
]