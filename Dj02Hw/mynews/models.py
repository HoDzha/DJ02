from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class My_News_post(models.Model):
    user_name =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Моя Новость')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Моя Новость'
        verbose_name_plural = 'Мои Новости'

# Create your models here.
