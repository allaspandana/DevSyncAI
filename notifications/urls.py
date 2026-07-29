from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.notification_list,
        name='notification_list'
    ),

    path(
        '<int:id>/read/',
        views.mark_as_read,
        name='mark_as_read'
    ),

    path(
        'activity/',
        views.activity_list,
        name='activity_list'
    ),
]