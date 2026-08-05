from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.contrib.auth import get_user_model

User = get_user_model()
@login_required
def task_list(request):

    tasks = Task.objects.all()


    search = request.GET.get('search')

    status = request.GET.get('status')

    priority = request.GET.get('priority')

    assigned = request.GET.get('assigned')



    if search:

        tasks = tasks.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )


    if status:

        tasks = tasks.filter(status=status)


    if priority:

        tasks = tasks.filter(priority=priority)


    if assigned:

        tasks = tasks.filter(assigned_to_id=assigned)



    paginator = Paginator(tasks,10)


    page_number = request.GET.get('page')


    tasks = paginator.get_page(page_number)



    context = {

        'tasks': tasks,

        'users': User.objects.all(),

    }


    return render(
        request,
        'tasks/task_list.html',
        context
    )
@login_required
def create_task(request):

    if request.method=="POST":

        form=TaskForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request,"Task created successfully.")

            return redirect('task_list')

    else:

        form=TaskForm()

    return render(request,
                  'tasks/create_task.html',
                  {'form':form})
@login_required
def task_detail(request,id):

    task=get_object_or_404(Task,id=id)

    return render(request,
                  'tasks/task_detail.html',
                  {'task':task})

@login_required

@login_required
def update_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            messages.success(request, "Task updated successfully.")

            return redirect('task_list')

    else:

        form = TaskForm(instance=task)

    return render(request,
                  'tasks/update_task.html',
                  {'form': form})
@login_required
def delete_task(request,id):

    task=get_object_or_404(Task,id=id)

    if request.method=="POST":

        task.delete()

        messages.success(request,
                         "Task deleted successfully.")

        return redirect('task_list')

    return render(request,
                  'tasks/delete_task.html',
                  {'task':task})