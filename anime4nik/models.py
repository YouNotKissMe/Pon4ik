from django.db import models
from django.contrib.auth.models import User
from anime.models import Anime


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    gender = models.CharField(choices=[('Муж', 'Муж'), ('Жен', 'Жен'), ('Хто я...', 'Хто я...')], verbose_name='Пол',
                              default='Хто я...', max_length=50)
    key = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    about = models.TextField(verbose_name='Расскажите о себе:', blank=True, null=True)
    picture = models.ImageField(verbose_name='Аватар', blank=True, null=True)
    anime = models.ManyToManyField(Anime)