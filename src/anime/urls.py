from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.AnimeListView.as_view(), name='anime'),
    path('anime/<int:pk>/', views.AnimeDetailView.as_view(), name='anime-id'),
    path('anime/genre/', views.GenreListView.as_view(), name='genre-list'),
    path(
        'anime/series/',
        views.AnimeSeriesListView.as_view(),
        name='series'
    ),
]
