from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Bug
from .forms import BugForm


@login_required
def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})


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