from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from teams.models import Team
from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from bugs.models import Bug



@login_required
def dashboard(request):

    role = request.user.role


    context = {

        "role": role,


        "total_teams":
            Team.objects.count(),


        "total_projects":
            Project.objects.count(),


        "total_sprints":
            Sprint.objects.count(),


        "total_tasks":
            Task.objects.count(),


        "total_bugs":
            Bug.objects.count(),


        "completed_tasks":
            Task.objects.filter(
                status="Completed"
            ).count(),


        "pending_tasks":
            Task.objects.exclude(
                status="Completed"
            ).count(),


        "open_bugs":
            Bug.objects.filter(
                status="Open"
            ).count(),


        "resolved_bugs":
            Bug.objects.filter(
                status="Resolved"
            ).count(),


        "recent_tasks":
            Task.objects.order_by(
                '-created_at'
            )[:5],


        "recent_bugs":
            Bug.objects.order_by(
                '-reported_date'
            )[:5]

    }


    return render(
        request,
        "dashboard/index.html",
        context
    )