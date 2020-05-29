from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *


from .models import Producto

def home(request):
	return render(request, 'tienda/home.html')
