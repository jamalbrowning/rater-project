from django.urls import path
from .views import top_five_games

urlpatterns = [
    path('reports/topfivegames', top_five_games)
]
