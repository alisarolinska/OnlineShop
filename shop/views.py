from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from shop.forms import CommentModelForm, OrderModelForm
from shop.models import Comment, Product, Order, Category


class ProductView(ListView):

	def get(self, *args, **kwargs):
		print('GET', args, kwargs)


def home_page(request):
	query = request.GET.get('query', None)
	if query is not None:  # text like "%...%"
		products = Product.objects.filter(description__icontains=query).order_by('-created_at')
		category = Category.objects.filter(description__icontains=query).order_by('-created_at')
	else:
		products = Product.objects.order_by('-created_at')
		category = Category.objects.order_by('-name')
	context = {
		'products': products,
		'categories': category,
		'current_user': request.user
	}
	return render(request, 'index.html', context)



def get_products_by_category(request, category):
	products = Product.objects.filter(category=category)
	response = f'<h1>Всего найдено {len(products)}<br></h1>'
	for product in products:
		response += f'{product.title}<br>'
	return HttpResponse(response)

"""
def get_product_detail(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		return HttpResponse(f'Товара с номером {product_id} не существует!')
	context = {
		'product': product,
		'comments': Comment.objects.filter(product=product_id).order_by('-id').all(),
		'comment_form': CommentModelForm(),
		'order_form': OrderModelForm()
	}
	return render(request, 'detail.html', context)
"""

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', context={'product':product})



@login_required(login_url='login')
def comment_views(request, product_id):
	if request.method == 'POST':
		form = CommentModelForm(request.POST)
		if form.is_valid():
			Comment.objects.create(
				user=request.user,
				text=form.data['text'],
				product=product_id
			)
		return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
	else:
		return redirect('home')


@login_required(login_url='login')
def order_views(request, product_id):
	if request.method == 'POST':
		form = OrderModelForm(request.POST)
		if form.is_valid():
			Order.objects.create(
				user=request.user,
				product=product_id
			)
			form.save()
	return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу

