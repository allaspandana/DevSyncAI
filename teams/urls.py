from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),

    path('create/', views.create_team, name='create_team'),

    path('<int:id>/', views.team_detail, name='team_detail'),

    path('<int:id>/edit/', views.update_team, name='update_team'),

    path('<int:id>/delete/', views.delete_team, name='delete_team'),
]