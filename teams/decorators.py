from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:

            if request.user.role == "ADMIN":
                return view_func(request, *args, **kwargs)

            else:
                raise PermissionDenied

        return redirect("login")

    return wrapper