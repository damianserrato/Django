# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    name = {
        "name":get_random_string(length=32)
    }
    return render(request, "random_world_generator_app/index.html", name)

def generate(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    # Alternative:
    # counter = request.session.get('counter', 0)
    # request.session['counter'] = counter + 1
    return redirect("/")

def end(request):
    request.session['counter'] = 0
    return redirect("/")