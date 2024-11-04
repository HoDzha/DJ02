from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    idata = {'page_title': 'Главная', 'name': 'Халил'}
    return render(request, 'main/home.html', idata)

def how_it_works(request):
    idata = {'page_title': 'Как работает ChatGpt'}
    return render(request, 'main/how_it_works.html', idata)

def my_experience(request):
    idata = {'page_title': 'Мой опыт'}
    return render(request, 'main/my_experience.html', idata)
def questions_contact(request):
    idata = {'page_title': 'Вопросы и контакты'}
    return render(request, 'main/questions_contact.html', idata)

