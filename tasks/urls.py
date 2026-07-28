from django.urls import path
from . import views

urlpatterns = [

    path('', views.task_list, name='task_list'),

    path('create/', views.create_task, name='create_task'),

    path('<int:id>/', views.task_detail, name='task_detail'),

    path('<int:id>/edit/', views.update_task, name='update_task'),

    path('<int:id>/delete/', views.delete_task, name='delete_task'),


]