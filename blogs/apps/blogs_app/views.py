# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse("Placeholder to display blog " + number)

def edit(request, number):
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request, number):
    return redirect('/')