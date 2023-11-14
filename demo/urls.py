from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("vehicles/", views.vehicles, name="Vehicles"),
    path('sense_vehicle/', views.sense_vehicle, name='sense_vehicle'),
]