from django import forms

from shop.models import Comment, Order
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CommentForm(forms.Form):
	text = forms.CharField(max_length=2000)
	choices = forms.ChoiceField(
		choices=[
			('issues', 'Issues'),
			('comment', 'Comment')
		]
	)


class CommentModelForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text']


class OrderModelForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
	update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

