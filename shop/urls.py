from django.urls import path

from shop import views

urlpatterns = [
    path('comment/<int:product_id>', views.comment_views, name='comment'),  # localhost:8000/shop/<int:product_id>/comment
    path('order/<int:product_id>', views.order_views, name='order'),  # localhost:8000/shop/<int:product_id>/order
    path('category', views.get_products_by_category),
    path('detail/<int:product_id>', views.get_product_detail),
    path(r'^$', views.cart_detail,
        name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$',
        views.cart_add,
        name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$',
        views.cart_remove,
        name='cart_remove')
	# path('путь', views.функция, имя_запроса)
]