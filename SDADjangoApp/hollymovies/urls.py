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
from django.urls import path

from viewer.views import (
    welcome, sum_numbers, create_genre, update_genre, delete_genre, list_genre,
    create_movie, MoviesView, MovieCreateView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', welcome, name='index'),
    path('sum/', sum_numbers),
    path('viewer/genres/create/', create_genre),
    path('viewer/genres/update/<s>/', update_genre),
    path('viewer/genres/delete/<s>/', delete_genre),
    path('viewer/genres/list/', list_genre, name='genre-list'),

    path('viewer/movies/create', MovieCreateView.as_view()),
    path('viewer/movies/list', MoviesView.as_view(), name='movie-list'),
]
