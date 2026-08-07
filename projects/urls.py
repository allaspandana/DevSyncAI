from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('', views.project_list, name='project_list'),

    path('create/', views.create_project, name='create_project'),

    path('<int:id>/', views.project_detail, name='project_detail'),

    path('<int:id>/edit/', views.update_project, name='update_project'),

    path('<int:id>/delete/', views.delete_project, name='delete_project'),
 path(
        'access-denied/',
        TemplateView.as_view(
            template_name='errors/403.html'
        ),
        name='access_denied'
    ),
]