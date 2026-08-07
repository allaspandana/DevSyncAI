from django.shortcuts import redirect
from django.contrib import messages


def role_required(allowed_roles=None):

    if allowed_roles is None:
        allowed_roles = []


    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            # Check user login
            if not request.user.is_authenticated:

                return redirect('login')


            # Check user role
            if request.user.role in allowed_roles:

                return view_func(
                    request,
                    *args,
                    **kwargs
                )


            # No permission
            messages.error(
                request,
                "You don't have permission to access this page."
            )

            return redirect('access_denied')


        return wrapper

    return decorator



# Only Admin
def admin_required(view_func):

    return role_required(
        ['ADMIN']
    )(view_func)



# Admin + Team Leader
def leader_required(view_func):

    return role_required(
        ['ADMIN', 'LEADER']
    )(view_func)



# Admin + Developer
def developer_required(view_func):

    return role_required(
        ['ADMIN', 'DEVELOPER']
    )(view_func)



# Admin + Tester
def tester_required(view_func):

    return role_required(
        ['ADMIN', 'TESTER']
    )(view_func)