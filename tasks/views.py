from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from .models import Task
from .forms import TaskForm
from accounts.decorators import role_required

User = get_user_model()


@login_required
def task_list(request):

    if request.user.role == "DEVELOPER":
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        tasks = Task.objects.all()

    search = request.GET.get("search")
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    status = request.GET.get("status")
    if status:
        tasks = tasks.filter(status=status)

    priority = request.GET.get("priority")
    if priority:
        tasks = tasks.filter(priority=priority)

    assigned = request.GET.get("assigned")
    if assigned:
        tasks = tasks.filter(assigned_to_id=assigned)

    paginator = Paginator(tasks, 10)
    page_number = request.GET.get("page")
    tasks = paginator.get_page(page_number)

    context = {
        "tasks": tasks,
        "users": User.objects.all(),
        "search": search,
        "status": status,
        "priority": priority,
        "assigned": assigned,
    }

    return render(request, "tasks/task_list.html", context)


@role_required(["ADMIN", "LEADER"])
def create_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully.")
            return redirect("task_list")

    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {
        "form": form
    })


@role_required(["ADMIN", "LEADER", "DEVELOPER"])
def update_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("task_list")

    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/update_task.html", {
        "form": form,
        "task": task
    })


@role_required(["ADMIN", "LEADER"])
def delete_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect("task_list")

    return render(request, "tasks/delete_task.html", {
        "task": task
    })


@login_required
def task_detail(request, id):

    task = get_object_or_404(Task, id=id)

    return render(request, "tasks/task_detail.html", {
        "task": task
    })