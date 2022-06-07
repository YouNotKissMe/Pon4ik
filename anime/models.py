from django.db import models


# Create your models here.
class Genre(models.Model):
    choice = ['сёнен', 'романтика', 'спорт']
    genre = models.CharField(max_length=100, verbose_name='Категория',
                             )
    def __str__(self):
        return self.genre

class Type(models.Model):
    choices = ['фильм',
               'сериал',
               'спешл',
               'клип'
        ,
               'ova',
               'ona'
               ]
    type = models.CharField(max_length=100, verbose_name='Тип',
                            )
    def __str__(self):
        return self.type


class Anonce(models.Model):
    choices = ['анонсированно',
               'выходит',
               'вышло',
               'приостановленно',
               'отменено']
    an = models.CharField(max_length=100, verbose_name='Статус',
                          )
    def __str__(self):
        return self.an


class Anime(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    status = models.ForeignKey(Anonce, on_delete=models.CASCADE,verbose_name='Статус')

    about = models.TextField(verbose_name='Описание')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр',
                              )
    typeAnime = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип',
                                  )
    trailer = models.FileField(verbose_name='Трейлер', blank=True, null=True)
    image = models.ImageField(verbose_name='Заглавная картинка', blank=True, null=True)
    links = models.TextField(verbose_name='Ссылки на источники для просмотра аниме', blank=True, null=True)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        return self.name
