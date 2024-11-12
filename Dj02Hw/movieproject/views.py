from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Create your views here.

def add_film(request):
    error = ""

    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        error = "Данные были заполнены некорректно"
        form = FilmForm()
    idata = {'page_title': 'Добавить фильм', 'form': form, 'error': error}
    return render(request, 'movieproject/add_film.html', idata)

def film_list(request):
    films = Film.objects.all()
    idata = {'page_title': 'Список фильмов', 'films': films}
    return render(request,'movieproject/film_list.html', idata)



# Create your views here.
