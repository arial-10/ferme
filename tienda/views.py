from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

def home(request):
	return render(request, 'tienda/home.html')


def home_admin(request):
    return render(request, 'tienda/admin/home.html')


def productos_admin(request):
    return render(request, 'tienda/admin/productos.html')
