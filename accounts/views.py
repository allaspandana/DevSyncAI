from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teams.models import Team
from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from bugs.models import Bug
from .forms import RegisterForm, LoginForm

def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Registration Successful!")

            return redirect("login")

        else:

            messages.error(request, "Please correct the errors below.")

    else:

        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )



def login_view(request):

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "Welcome Back!"
            )

            if user.role == "Admin":
                return redirect("dashboard")

            elif user.role == "Team Leader":
                return redirect("dashboard")

            elif user.role == "Developer":
                return redirect("dashboard")

            elif user.role == "Tester":
                return redirect("dashboard")

            else:
                return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid Username or Password."
            )

    else:

        form = LoginForm()

    return render(
        request,
        "registration/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged Out Successfully."
    )

    return redirect("login")
@login_required
def profile(request):

    user = request.user


    context = {

        'task_count': user.assigned_tasks.count(),

        'bug_count': user.assigned_bugs.count()

    }


    return render(
        request,
        'accounts/profile.html',
        context
    )
def home(request):
    return render(request, "home.html")
@login_required(login_url="login")
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
        "user": request.user,
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

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )