from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.forms import CommentModelForm, OrderModelForm, CartAddProductForm
from shop.models import Comment, Product, Order, Cart, Category


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
	products = Product.objects.filter(category = Category)
	response = f'<h1>Всего найдено {len(products)}<br></h1>'
	for product in products:
		response += f'{product.title}<br>'
	return HttpResponse(response)


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
		return redirect('all_tasks')


@login_required(login_url='login')
def order_views(request, product_id):
	if request.method == 'POST':
		form = OrderModelForm(request.POST)
		if form.is_valid():
			Order.objects.create(
				user = request.user,
				product = product_id
			)
			form.save()
	return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for product in cart:
        product['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': product['quantity'],
                'update': True
            })
    return render(request, 'cart/detail.html', {'cart': cart})
