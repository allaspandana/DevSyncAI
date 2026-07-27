from django.urls import path
from . import views

urlpatterns = [

    path('', views.sprint_list, name='sprint_list'),

    path('create/', views.create_sprint, name='create_sprint'),

    path('<int:id>/', views.sprint_detail, name='sprint_detail'),

    path('<int:id>/edit/', views.update_sprint, name='update_sprint'),

    path('<int:id>/delete/', views.delete_sprint, name='delete_sprint'),

]