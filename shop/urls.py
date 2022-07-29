from django.urls import path

from shop import views

urlpatterns = [
    path('comment/<int:product_id>', views.comment_views, name='comment'),  # localhost:8000/shop/<int:product_id>/comment
    path('order/<int:product_id>', views.order_views, name='order'),  # localhost:8000/shop/<int:product_id>/order
    path('category/<int:category>', views.get_products_by_category, name='category'),
    path('detail/<int:id>', views.product_detail_view, name='product-detail')
	# path('путь', views.функция, имя_запроса)
]