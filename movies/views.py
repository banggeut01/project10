from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ReviewForm
from .models import Movie,Review
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/index.html',context)

def detail(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form
    }
    return render(request,'movies/detail.html',context)

@require_POST
def new(request,movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie,pk=movie_pk)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            form = review_form.save(commit=False)
            form.user = request.user
            form.movie = movie
            form.save()
            return redirect('movies:detail',movie_pk)
    else:
        return redirect('accounts:login')

@require_POST
def delete(request,movie_pk,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('movies:detail',movie_pk)

@require_POST
def like(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.user.is_authenticated:
        if request.user in movie.like_user.all():
            movie.like_user.remove(request.user)
        else:
            movie.like_user.add(request.user)
            
        return redirect('movies:detail', movie_pk)
    else:
        return redirect('accounts:login')