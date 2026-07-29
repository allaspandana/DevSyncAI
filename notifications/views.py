from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Notification, ActivityLog


# Display logged-in user's notifications
@login_required
def notification_list(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'notifications/notification_list.html',
        {
            'notifications': notifications
        }
    )


# Mark notification as read
@login_required
def mark_as_read(request, id):

    notification = get_object_or_404(
        Notification,
        id=id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    messages.success(
        request,
        "Notification marked as read."
    )

    return redirect('notification_list')



# Display Activity Logs
@login_required
def activity_list(request):

    activities = ActivityLog.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'notifications/activity_list.html',
        {
            'activities': activities
        }
    )