from django.urls import path
from .views import main_animes, anime_page,genre,type,anonce,anime_add

urlpatterns = [
    path('', main_animes, name='all_anime'),
    path('<int:pk>/', anime_page, name='anime_page'),
    path('type/<int:pk>/', type, name='type_page'),
    path('an/<int:pk>/', anonce, name='an_page'),
    path('genre/<int:pk>/', genre, name='genre_page'),
    path('add/<int:pk>/', anime_add, name='add'),
]
