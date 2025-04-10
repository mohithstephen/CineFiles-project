from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Genre, Movie, Watchlist, Rating
from django.http import HttpResponse

def dashboard(request):
    genres = Genre.objects.all()  # Fetch all genres from the database
    return render(request, 'cinefiles_app/dashboard.html', {'genres': genres})

def genre_page(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = Movie.objects.filter(genre=genre)  # Fetch movies of the selected genre

    # Fetch the user's ratings
    user_ratings = {}
    if request.user.is_authenticated:
        user_ratings = {rating.movie_id: rating.rating for rating in Rating.objects.filter(user=request.user)}

    # Add user-specific data to each movie
    for movie in movies:
        movie.user_rating = user_ratings.get(movie.id, None)

    return render(request, 'cinefiles_app/genre_page.html', {
        'genre': genre,
        'movies': movies,
    })

def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user.is_authenticated:
        watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)
        if created:
            messages.success(request, f'"{movie.title}" has been added to your watchlist!')
        else:
            messages.info(request, f'"{movie.title}" is already in your watchlist.')
    else:
        messages.error(request, "You need to log in to add movies to your watchlist.")
    return redirect('genre_page', genre_id=movie.genre.id)

def rate_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        if request.user.is_authenticated:
            rating_value = int(request.POST.get('rating', 0))
            if 1 <= rating_value <= 5:  # Ensure the rating is between 1 and 5
                rating, created = Rating.objects.update_or_create(
                    user=request.user,
                    movie=movie,
                    defaults={'rating': rating_value}
                )
                messages.success(request, f'You rated "{movie.title}" {rating_value} stars!')
            else:
                messages.error(request, "Invalid rating value. Please select a value between 1 and 5.")
        else:
            messages.error(request, "You need to log in to rate movies.")
        return redirect('genre_page', genre_id=movie.genre.id)
    return HttpResponse("Invalid request method.", status=405)