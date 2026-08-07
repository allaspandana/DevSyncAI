from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from .models import Bug
from .forms import BugForm
from accounts.decorators import role_required


User = get_user_model()


# Bug List
@login_required
def bug_list(request):

    bugs = Bug.objects.all()

    # Search
    search = request.GET.get('search')

    if search:
        bugs = bugs.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )


    # Filter severity
    severity = request.GET.get('severity')

    if severity:
        bugs = bugs.filter(
            severity=severity
        )


    # Filter status
    status = request.GET.get('status')

    if status:
        bugs = bugs.filter(
            status=status
        )


    # Filter assigned developer
    assigned = request.GET.get('assigned')

    if assigned:
        bugs = bugs.filter(
            assigned_to_id=assigned
        )


    # Pagination
    paginator = Paginator(
        bugs,
        10
    )

    page_number = request.GET.get('page')

    bugs = paginator.get_page(page_number)


    context = {
        "bugs": bugs,
        "search": search,
        "severity": severity,
        "status": status,
        "assigned": assigned,
        "users": User.objects.all(),
    }


    return render(
        request,
        "bugs/bug_list.html",
        context
    )



# Create Bug
@role_required(
    [
        'ADMIN',
        'TESTER'
    ]
)
def create_bug(request):

    if request.method == "POST":

        form = BugForm(request.POST)

        if form.is_valid():

            bug = form.save(commit=False)

            # Automatically set logged-in user
            bug.reported_by = request.user

            bug.save()

            messages.success(
                request,
                "Bug created successfully."
            )
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(
        request,
        'bugs/create_bug.html',
        {
            'form': form
        }
    )


# Bug Detail
@login_required
def bug_detail(request, id):

    bug = get_object_or_404(
        Bug,
        id=id
    )


    return render(
        request,
        "bugs/bug_detail.html",
        {
            "bug": bug
        }
    )



# Update Bug
@role_required(["ADMIN", "DEVELOPER"])
def update_bug(request, id):

    bug = get_object_or_404(
        Bug,
        id=id
    )


    if request.method == "POST":

        form = BugForm(
            request.POST,
            instance=bug
        )


        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Bug updated successfully."
            )

            return redirect(
                "bug_list"
            )


    else:

        form = BugForm(
            instance=bug
        )


    return render(
        request,
        "bugs/update_bug.html",
        {
            "form": form,
            "bug": bug
        }
    )



# Delete Bug
@role_required(["ADMIN"])
def delete_bug(request, id):

    bug = get_object_or_404(
        Bug,
        id=id
    )


    if request.method == "POST":

        bug.delete()

        messages.success(
            request,
            "Bug deleted successfully."
        )

        return redirect(
            "bug_list"
        )
    return render(
        request,
        "bugs/delete_bug.html",
        {
            "bug": bug
        }
    )