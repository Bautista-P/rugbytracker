from django.urls import path
from . import views

app_name = 'jugadores'
urlpatterns = [
    path('', views.tackles, name='tackles'),
    path('increment_tackles/<int:jugador_id>/', views.increment_tackles, name='increment_tackles'),
    path('decrement_tackles/<int:jugador_id>/', views.decrement_tackles, name='decrement_tackles'),
    ]

