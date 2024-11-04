from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('how_it_works', views.how_it_works, name='how_it_works'),
    path('my_experience', views.my_experience, name='my_experience'),
    path('questions_contact', views.questions_contact, name='questions_contact')

]
