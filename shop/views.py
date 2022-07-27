from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.forms import CommentModelForm, OrderModelForm
from shop.models import Comment, Product


def home_page(request):
    return render(request, 'index.html')


def get_products_by_category(request, category):
	products = Product.objects.filter(category = category)
	response = f'<h1>Всего найдено {len(products)}<br></h1>'
	for product in products:
		response += f'{product.title}<br>'
	return HttpResponse(response)


def get_product_detail(request, product_id):
	try:
		task = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		return HttpResponse(f'Задачи с номером {product_id} не существует!')
	context = {
		'task': task,
		'comments': Comment.objects.filter(task_id=product_id).order_by('-id').all(),
		'comment_form': CommentModelForm(),

	}
	return render(request, 'detail.html', context)


def comment_views(request, task_id):
	if request.method == 'POST':
		form = CommentModelForm(request.POST)
		if form.is_valid():
			Comment.objects.create(
				user=request.user,
				text=form.data['text'],
				task_id=task_id
			)
		return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
	else:
		return redirect('all_tasks')



def order_views(request):
	if request.method == 'POST':
		form = OrderModelForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу

