# forms.py
from .models import My_News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class My_News_postForm(ModelForm):
	class Meta:
		model = My_News_post
		fields = ['user_name', 'title', 'short_description', 'text', 'pub_date']
		widgets = {
			'user_name': TextInput(attrs={'class': 'form-control col-6', 'placeholder': 'Автор новости'}),
			'title': TextInput(attrs={'class': 'form-control col-6', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(
				attrs={'class': 'form-control col-12', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control col-12', 'placeholder': 'Содержание новости', 'rows': 4}),
			'pub_date': DateTimeInput(
				attrs={'class': 'form-control col-4', 'placeholder': 'Дата публикации', 'type': 'datetime-local'}),
		}