from django.shortcuts import render
from .models import My_News_post
from .forms import My_News_postForm
# Create your views here.
def home(request):
    news = My_News_post.objects.all()
    idata = {'page_title': 'Новости', 'name': 'Халил', 'news': news}
    return render(request, 'mynews/my_news.html', idata)

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = My_News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('mynews_home')
        else:
            error = "Данные были заполнены некорректно"
    form = My_News_postForm()
    return render(request, 'mynews/add_new_post.html', {'form': form, 'error': error})

