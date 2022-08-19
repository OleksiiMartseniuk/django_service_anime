from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimeListView.as_view(), name='anime'),
    path('<int:pk>/', views.AnimeDetailView.as_view(), name='anime-id'),
    path('genre/', views.GenreListView.as_view(), name='genre-list'),
    path('series/', views.AnimeSeriesListView.as_view(), name='series'),
]
