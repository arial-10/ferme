from django.http import HttpResponse
from django.shortcuts import render, redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin')
        else:
            return view_func(request, *args, *kwargs)

    return wrapper_func

def autorizar_usuarios(roles_permitidos=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in roles_permitidos:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Usted no cuenta con los privilegios necesarios '
                    + 'para ver esta sección.')
        return wrapper_func
    return decorator

def solo_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'administrador' or group == 'vendedor' or group == 'empleado' or group == 'proveedor':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func
