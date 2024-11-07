from django.shortcuts import render
from .models import News_post
# Create your views here.
def home(request):
    news = News_post.objects.all()
    idata = {'page_title': 'Новости', 'name': 'Халил', 'news': news}
    return render(request, 'news/news.html', idata)


