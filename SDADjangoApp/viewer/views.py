from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from viewer.forms import MovieForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from viewer.models import Genre, Movie

from django.shortcuts import render

LOGGER = getLogger()


def welcome(request):
    name_request = request.GET.get('name', '')
    city_request = request.GET.get('city', '')
    return render(
        request, template_name="welcome.html",
        context={
            'name': name_request,
            'city': city_request
        }
    )


def sum_numbers(request):
    number1 = request.GET.get('value1', 0)
    number2 = request.GET.get('value2', 0)
    result = int(number1) + int(number2)

    return HttpResponse(f"The sum for numbers {number1} and {number2} is {result}")


def create_genre(request):

    name_request = request.GET.get('name', None)

    if name_request is None:
        return HttpResponse("Please, give a valid name for the genre in the query string 'name'")

    genre = Genre.objects.create(name=name_request)

    return HttpResponse(f"Genre has been created with id {genre.id}")


def update_genre(request, s):
    name_request = request.GET.get('name', None)

    genre = Genre.objects.get(id=int(s))
    genre.name = name_request
    genre.save()

    return HttpResponse(f"The genre has been updated to {genre.name}")


def delete_genre(request, s):
    if request.method == "GET":
        movie = Movie.objects.get(id=s)
        return render(
            request, template_name='movie/confirm_delete.html',
            context={
                'object': movie
            }
        )
    else:
        if not Movie.objects.filter(id=int(s)).exists():
            return HttpResponse(f"The genre with id {s} does not exist")

        Movie.objects.get(id=int(s)).delete()

        return HttpResponse(f"The genre with id {s} has been removed")



@login_required
def list_genre(request):
    name_filter = request.GET.get('name', None)
    is_favorite_filter = request.GET.get('favorite', None)

    genres = Genre.objects.all()
    if name_filter:
        genres = genres.filter(name__startswith=name_filter)

    if is_favorite_filter:
        genres = genres.filter(is_favorite=is_favorite_filter)

    return render(
        request, template_name="genre/list.html",
        context={
            'list_genre': genres
        }
    )


def create_movie(request):

    title_req = request.GET.get('title', None)
    rating_req = request.GET.get('rating', 0)
    released_req = request.GET.get('released', None)
    description_req = request.GET.get('description', None)
    genre_id_req = request.GET.get('genre_id', None)

    movie = Movie(
        title=title_req,
        rating=rating_req,
        released=released_req,
        description=description_req,
        genre=Genre.objects.get(id=genre_id_req)
    )
    movie.save()

    return HttpResponse(f"Movie has been created with id {movie.id}")


class MoviesView(LoginRequiredMixin, ListView):
    template_name = "movie/list.html"
    model = Movie


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "movie/create_form.html"
    form_class = MovieForm
    success_url = reverse_lazy("success")
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while creating a movie.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "movie/create_form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("success")
    permission_required = 'viewer.change_movie'


class MovieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'movie/confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movie-list')
    permission_required = 'viewer.delete_movie'

