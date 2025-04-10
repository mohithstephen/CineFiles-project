from django.db import models
from django.contrib.auth.models import User

# Genre model to define movie genres
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image_url = models.URLField()  # URL for the genre card image

    def __str__(self):
        return self.name

# Movie model to store movie details
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    poster_url = models.URLField()  # URL for the movie poster
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

# Watchlist model to store user-specific watchlist
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watchlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rated_by')
    rating = models.PositiveSmallIntegerField()  # Rating out of 5
    rated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'movie')  # Prevent multiple ratings for the same movie by the same user

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.rating}"