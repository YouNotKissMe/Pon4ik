from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, AuthUserForm,HunterForm
from .models import Users
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView, CreateView
from anime.models import Anime

def user_cabinet(request):

    if request.user.is_authenticated:
        #a = Anime.objects.get(users__anime=request.user.users.pk)
        #print(len(a))
        return render(request,'user_page.html',{'user':request.user})
    else:
        return render('registration/login.html',request)

def my_anime(request):
    if request.user.is_authenticated:
        #a = Anime.objects.get(users__anime=request.user.users.pk)
        #print(len(a))
        print(Anime.objects.filter(users__pk=request.user.users.pk))
        return render(request,'my_anime.html',{'anime':Anime.objects.filter(users__pk=request.user.users.pk)})
    else:
        return render('registration/login.html',request)

class RegisterFormView(FormView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('log')
    template_name = 'registration_page.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginViews(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('profile')

class ProfileView(CreateView):
    template_name = 'add_information_user.html'
    form_class = HunterForm
    model = Users
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.key = self.request.user
        obj.first_name = self.request.user.first_name
        obj.last_name = self.request.user.last_name
        obj.save()
        return HttpResponseRedirect(self.success_url)

class ProfileUpdateView(UpdateView):
    model = Users
    template_name = 'user_update_page.html'
    fields = ['first_name', 'last_name', 'gender', 'birth_date', 'about',
              'picture']
    success_url = reverse_lazy('profile')