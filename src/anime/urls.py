from django.urls import path
from . import views

urlpatterns = [
    path('anime/anons/', views.AnimeAnonsListView.as_view()),
    path('anime/<int:pk>/', views.AnimeDetailView.as_view()),
]
