from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('genre/<int:genre_id>/', views.genre_page, name='genre_page'),
    path('add-to-watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('rate-movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('watchlist/', views.watchlist_page, name='watchlist_page'),
    path('remove-from-watchlist/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('ratings/', views.ratings_page, name='ratings_page'),
    path('add-movie/', views.add_movie, name='add_movie'),
]