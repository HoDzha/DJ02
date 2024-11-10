from .models import My_News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class My_News_postForm(ModelForm):
	class Meta:
		model = My_News_post
		fields = ['user_name', 'title', 'short_description', 'text', 'pub_date']
		widgets = {
			'user_name': Label(attrs={'class': 'form-control', 'placeholder': 'Автор новости'}),
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
		}