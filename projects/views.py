from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Project
from .forms import ProjectForm
from accounts.decorators import role_required


# Project List
@login_required
def project_list(request):

    projects = Project.objects.all()

    search = request.GET.get('search')
    status = request.GET.get('status')
    priority = request.GET.get('priority')

    if status:
        projects = projects.filter(status=status)

    if priority:
        projects = projects.filter(priority=priority)

    if search:
        projects = projects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    paginator = Paginator(projects, 10)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'projects': projects,
        'search': search,
        'status': status,
        'priority': priority,
    }

    return render(request, 'projects/project_list.html', context)


# Create Project
@role_required(['ADMIN', 'LEADER'])
def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Project created successfully.")
            return redirect('project_list')

    else:
        form = ProjectForm()

    return render(
        request,
        'projects/create_project.html',
        {
            'form': form
        }
    )


# Project Detail
@login_required
def project_detail(request, id):

    project = get_object_or_404(Project, id=id)

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project
        }
    )


# Update Project
@role_required(['ADMIN', 'LEADER'])
def update_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('project_list')

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'projects/update_project.html',
        {
            'form': form,
            'project': project
        }
    )


# Delete Project
@role_required(['ADMIN'])
def delete_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('project_list')

    return render(
        request,
        'projects/delete_project.html',
        {
            'project': project
        }
    )