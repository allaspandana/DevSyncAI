from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .models import Bug
from .forms import BugForm

User = get_user_model()
@login_required
def bug_list(request):

    bugs = Bug.objects.all()

    search = request.GET.get('search')
    severity = request.GET.get('severity')
    status = request.GET.get('status')
    assigned = request.GET.get('assigned')

    # Search by title or description
    if search:
        bugs = bugs.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # Filter by severity
    if severity:
        bugs = bugs.filter(severity=severity)

    # Filter by status
    if status:
        bugs = bugs.filter(status=status)

    # Filter by assigned developer
    if assigned:
        bugs = bugs.filter(assigned_to__id=assigned)

    # Pagination
    paginator = Paginator(bugs, 10)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)

    context = {
        'bugs': bugs,
        'search': search,
        'severity': severity,
        'status': status,
        'assigned': assigned,
        'users': User.objects.all(),
    }

    return render(request, 'bugs/bug_list.html', context)

@login_required
def create_bug(request):

    if request.method == "POST":

        form = BugForm(request.POST)

        if form.is_valid():

            bug = form.save(commit=False)

            # Automatically set the logged-in user
            bug.reported_by = request.user

            # Save the bug
            bug.save()

            messages.success(request, "Bug created successfully.")

            return redirect("bug_list")

    else:
        form = BugForm()

    return render(request, 'bugs/create_bug.html', {'form': form})


@login_required
def bug_detail(request, id):

    bug = get_object_or_404(Bug, id=id)

    return render(request, 'bugs/bug_detail.html', {'bug': bug})


@login_required
def update_bug(request, id):

    bug = get_object_or_404(Bug, id=id)

    if request.method == "POST":

        form = BugForm(request.POST, instance=bug)

        if form.is_valid():

            updated_bug = form.save(commit=False)

            # Validate resolved date
            if (
                updated_bug.resolved_date and
                updated_bug.resolved_date < bug.reported_date.date()
            ):
                form.add_error(
                    "resolved_date",
                    "Resolved date cannot be earlier than reported date."
                )
            else:
                updated_bug.save()

                messages.success(
                    request,
                    "Bug updated successfully."
                )

                return redirect("bug_list")

    else:
        form = BugForm(instance=bug)

    return render(
        request,
        'bugs/update_bug.html',
        {
            'form': form,
            'bug': bug
        }
    )


@login_required
def delete_bug(request, id):

    bug = get_object_or_404(Bug, id=id)

    if request.method == "POST":

        bug.delete()

        messages.success(
            request,
            "Bug deleted successfully."
        )

        return redirect("bug_list")

    return render(
        request,
        'bugs/delete_bug.html',
        {'bug': bug}
    )