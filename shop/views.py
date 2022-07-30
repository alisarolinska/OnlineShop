from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from shop.forms import OrderCreateForm
from shop.models import Product, Category


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



def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', context={'product':product})



@login_required(login_url='login')
def order_create(request):
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect(request.headers.get('Referer'))


def order_page(request):
	return render(request, 'orders.html')
