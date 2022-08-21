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
    )
]
