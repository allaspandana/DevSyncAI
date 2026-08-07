from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Team
from .forms import TeamForm

from accounts.decorators import admin_required


# ==========================
# Team List
# ==========================

@login_required
def team_list(request):

    teams = Team.objects.all()

    return render(
        request,
        'teams/team_list.html',
        {
            'teams': teams
        }
    )


# ==========================
# Create Team
# ==========================

@admin_required
def create_team(request):

    if request.method == "POST":

        form = TeamForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('team_list')

    else:

        form = TeamForm()


    return render(
        request,
        'teams/create_team.html',
        {
            'form': form
        }
    )


# ==========================
# Team Detail
# ==========================

@login_required
def team_detail(request, id):

    team = get_object_or_404(
        Team,
        id=id
    )


    return render(
        request,
        'teams/team_detail.html',
        {
            'team': team
        }
    )


# ==========================
# Update Team
# ==========================

@admin_required
def update_team(request, id):

    team = get_object_or_404(
        Team,
        id=id
    )


    if request.method == "POST":

        form = TeamForm(
            request.POST,
            instance=team
        )


        if form.is_valid():

            form.save()

            return redirect('team_list')


    else:

        form = TeamForm(
            instance=team
        )


    return render(
        request,
        'teams/update_team.html',
        {
            'form': form,
            'team': team
        }
    )


# ==========================
# Delete Team
# ==========================

@admin_required
def delete_team(request, id):

    team = get_object_or_404(
        Team,
        id=id
    )


    if request.method == "POST":

        team.delete()

        return redirect('team_list')


    return render(
        request,
        'teams/delete_team.html',
        {
            'team': team
        }
    )