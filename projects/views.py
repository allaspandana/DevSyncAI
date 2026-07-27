from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Project
from .forms import ProjectForm
@login_required
def project_list(request):

    projects = Project.objects.all()

    return render(request,
                  'projects/project_list.html',
                  {'projects': projects})
@login_required
def create_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request,
                             "Project created successfully.")

            return redirect('project_list')

    else:

        form = ProjectForm()

    return render(request,
                  'projects/create_project.html',
                  {'form': form})
@login_required
def project_detail(request, id):

    project = get_object_or_404(Project, id=id)

    return render(request,
                  'projects/project_detail.html',
                  {'project': project})
@login_required
def update_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':

        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():

            form.save()

            messages.success(request,
                             "Project updated successfully.")

            return redirect('project_list')

    else:

        form = ProjectForm(instance=project)

    return render(request,
                  'projects/update_project.html',
                  {
                      'form': form,
                      'project': project
                  })
@login_required
def delete_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':

        project.delete()

        messages.success(request,
                         "Project deleted successfully.")

        return redirect('project_list')

    return render(request,
                  'projects/delete_project.html',
                  {'project': project})