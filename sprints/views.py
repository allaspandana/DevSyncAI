from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Sprint
from .forms import SprintForm
from accounts.decorators import role_required


# Sprint List
@login_required
def sprint_list(request):
    sprints = Sprint.objects.all()

    return render(
        request,
        'sprints/sprint_list.html',
        {'sprints': sprints}
    )


# Create Sprint
@role_required(['ADMIN', 'LEADER'])
def create_sprint(request):

    if request.method == "POST":
        form = SprintForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Sprint created successfully.")
            return redirect('sprint_list')

    else:
        form = SprintForm()

    return render(
        request,
        'sprints/create_sprint.html',
        {
            'form': form
        }
    )


# Sprint Detail
@login_required
def sprint_detail(request, id):

    sprint = get_object_or_404(Sprint, id=id)

    return render(
        request,
        'sprints/sprint_detail.html',
        {
            'sprint': sprint
        }
    )


# Update Sprint
@role_required(['ADMIN', 'LEADER'])
def update_sprint(request, id):

    sprint = get_object_or_404(Sprint, id=id)

    if request.method == "POST":
        form = SprintForm(request.POST, instance=sprint)

        if form.is_valid():
            form.save()
            messages.success(request, "Sprint updated successfully.")
            return redirect('sprint_list')

    else:
        form = SprintForm(instance=sprint)

    return render(
        request,
        'sprints/update_sprint.html',
        {
            'form': form,
            'sprint': sprint
        }
    )


# Delete Sprint
@role_required(['ADMIN', 'LEADER'])
def delete_sprint(request, id):

    sprint = get_object_or_404(Sprint, id=id)

    if request.method == "POST":
        sprint.delete()
        messages.success(request, "Sprint deleted successfully.")
        return redirect('sprint_list')

    return render(
        request,
        'sprints/delete_sprint.html',
        {
            'sprint': sprint
        }
    )