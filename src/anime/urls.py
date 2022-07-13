from django.urls import path
from . import views

urlpatterns = [
    path(
        'anime/schedule-day/',
         views.AnimeScheduleDayView.as_view(),
         name='schedule-day'
    ),
    path('anime/anons/', views.AnimeAnonsListView.as_view(), name='anons'),
    path('anime/<int:pk>/', views.AnimeDetailView.as_view(), name='anime-id'),
]
