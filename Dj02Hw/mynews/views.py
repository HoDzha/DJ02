from django.shortcuts import render
from .models import My_News_post
# Create your views here.
def home(request):
    news = My_News_post.objects.all()
    idata = {'page_title': 'Новости', 'name': 'Халил', 'news': news}
    return render(request, 'mynews/my_news.html', idata)

