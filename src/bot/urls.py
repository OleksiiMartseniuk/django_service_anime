from django.urls import path

from . import views

urlpatterns = [
    path(
        'statistic/',
        views.StatisticsBotView.as_view(),
        name='create-statistic'
    ),
    path(
        'massage/',
        views.BotCollBackMessageView.as_view(),
        name='create-massage'
    )
]
