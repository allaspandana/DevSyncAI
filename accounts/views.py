from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required(login_url="login")
def dashboard(request):
    return render(
        request,
        "dashboard/dashboard.html",
        {"user": request.user}
    )