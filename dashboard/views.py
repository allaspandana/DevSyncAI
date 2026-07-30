from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from teams.models import Team
from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from bugs.models import Bug


@login_required
def dashboard(request):

    total_teams = Team.objects.count()
    total_projects = Project.objects.count()
    total_sprints = Sprint.objects.count()
    total_tasks = Task.objects.count()
    total_bugs = Bug.objects.count()

    completed_tasks = Task.objects.filter(status="Completed").count()
    pending_tasks = Task.objects.filter(status="To Do").count()

    open_bugs = Bug.objects.filter(status="Open").count()
    resolved_bugs = Bug.objects.filter(status="Resolved").count()

    recent_tasks = Task.objects.order_by("-created_at")[:5]
    recent_bugs = Bug.objects.order_by("-reported_date")[:5]

    context = {
        "total_teams": total_teams,
        "total_projects": total_projects,
        "total_sprints": total_sprints,
        "total_tasks": total_tasks,
        "total_bugs": total_bugs,

        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,

        "open_bugs": open_bugs,
        "resolved_bugs": resolved_bugs,

        "recent_tasks": recent_tasks,
        "recent_bugs": recent_bugs,
    }

    return render(request, "dashboard/dashboard.html", context)