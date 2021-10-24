"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView

from viewer.views import (
    welcome, sum_numbers, create_genre, update_genre, delete_genre, list_genre,
    create_movie, MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, OwnPasswordChange,
    OwnPasswordChangeDone
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', welcome, name='index'),
    path('sum/', sum_numbers),
    path('viewer/genres/create/', create_genre),
    path('viewer/genres/update/<s>/', update_genre),
    path('viewer/genres/delete/<s>/', delete_genre),
    path('viewer/genres/list/', list_genre, name='genre-list'),

    path('viewer/movies/create', MovieCreateView.as_view(), name='movie-create'),
    path('viewer/movies/update/<pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('viewer/movies/delete/<pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('viewer/movies/list/', MoviesView.as_view(), name='movie-list'),

    path('viewer/success', TemplateView.as_view(template_name="success.html"), name="success"),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', OwnPasswordChange.as_view(), name='change'),
    path('password_change/done/', OwnPasswordChangeDone.as_view(), name='password_change_done'),
]
