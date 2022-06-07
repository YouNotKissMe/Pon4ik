from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Anime, Genre, Type, Anonce
from anime4nik.models import Users



# Create your views here.

def main_animes(request):
    if 'search' in request.GET and request.GET['search']:
        if Anime.objects.filter(name__icontains=request.GET['search']):
            anime = Anime.objects.filter(name__icontains=request.GET['search'])
        else:
            anime = Anime.objects.all()
    else:
        anime = Anime.objects.all()
    genre = Genre.objects.all()
    type = Type.objects.all()
    an = Anonce.objects.all()
    return render(request, 'all_anime.html', {'anime': anime, 'an': an, 'type': type, 'genre': genre})


def genre(request, pk):
    anime = Anime.objects.filter(genre__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def type(request, pk):
    anime = Anime.objects.filter(typeAnime__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def anonce(request, pk):
    anime = Anime.objects.filter(status__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def anime_page(request, pk):
    anime = Anime.objects.get(pk=pk)


    return render(request, 'anime_page.html', {'anime': anime})

def anime_add(request,pk):

    request.user.users.anime.add(Anime.objects.get(pk=pk))
    return redirect('profile')
#
# class AnimeUpdateView(UpdateView):
#     model = Users
#     template_name = 'add_anime.html'
#     fields = ('first_name',)
#     success_url = reverse_lazy('all_anime')
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.key = self.request.user
#
#         obj.save()
#         return HttpResponseRedirect(self.success_url)



