from django.urls import path

from . import views

urlpatterns = [
    path(
        'statistic/',
        views.StatisticsBotView.as_view(),
        name='create-statistic'
    ),
    path(
        'message/',
        views.BotCollBackMessageView.as_view(),
        name='create-massage'
    ),
    path(
        'create-user/',
        views.BotUserCreateView.as_view(),
        name='create-user'
    ),
    path(
        'add-anime/',
        views.AddAnimeUserView.as_view(),
        name='add-anime'
    ),
    path(
        'remove-anime/',
        views.RemoveAnimeUserView.as_view(),
        name='remove-anime'
    )
]
