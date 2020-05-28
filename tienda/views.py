from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages


from .models import Producto

def home(request):
	return render(request, 'tienda/home.html')