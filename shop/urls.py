from django.urls import path

from shop import views

urlpatterns = [
    path('comment/<int:product_id>', views.comment_views, name='comment'),  # localhost:8000/shop/<int:product_id>/comment
    #path('order', views.order_views, name='order'),  # localhost:8000/shop/order
    path('category', views.get_products_by_category),
    path('detail/<int:product_id>', views.get_product_detail)
	# path('путь', views.функция, имя_запроса)
]