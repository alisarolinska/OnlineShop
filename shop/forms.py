from django import forms

from shop.models import Comment, Order


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


