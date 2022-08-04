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
	products = Product.objects.order_by('-created_at')
	category = Category.objects.order_by('-name')
	context = {
		'products': products,
		'categories': category,
		'current_user': request.user
	}
	return render(request, 'home.html', context)



def get_products_by_category(request, category):
	context = {
		'products': Product.objects.filter(category=category),
		'category': Category.objects.get(pk=category),
		'current_user': request.user
	}
	return render(request, 'category.html', context)



def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', context={'product':product})



@login_required(login_url='login')
def order_create(request, product_id):
	if request.method == 'GET':
		form = OrderCreateForm()
		return render(request, 'orders.html', context={'order_form': form,
													   'product':product_id
													   })
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'home.html')


