from django.urls import path
from .views import LoginViews, RegisterFormView, ProfileView, ProfileUpdateView, user_cabinet,my_anime
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', user_cabinet, name='profile'),
    path('login/', LoginViews.as_view(), name='log'),
    path('logged_out/', LogoutView.as_view(), name='logout'),
    path('registrations/', RegisterFormView.as_view(), name='reg'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='update_old_hunter'),
    path('supp/', ProfileView.as_view(), name='add_a_new_hunter'),
    path('anime/', my_anime, name='my_anime')
]