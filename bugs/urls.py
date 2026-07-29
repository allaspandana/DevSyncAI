from django.urls import path
from . import views

urlpatterns = [

    path('', views.bug_list, name='bug_list'),

    path('create/', views.create_bug, name='create_bug'),

    path('<int:id>/', views.bug_detail, name='bug_detail'),

    path('<int:id>/edit/', views.update_bug, name='update_bug'),

    path('<int:id>/delete/', views.delete_bug, name='delete_bug'),
]