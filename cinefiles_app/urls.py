from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('genre/<int:genre_id>/', views.genre_page, name='genre_page'),
    path('add-to-watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('rate-movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
]