# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages

def index(request):
    return render(request, 'thewall_app/index.html')

def register(request):
    check = User.objects.register(
        request.POST['name'],
        request.POST['username'],
        request.POST['email'],
        request.POST['password'],
        request.POST['confirm']
    )

    if not check["valid"]:
        for error in check["errors"]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/")

    else:
        request.session["user_id"] = check["user"].id
        messages.add_message(request, messages.SUCCESS, "Registration Successful!!, {}".format(request.POST["username"]))
        return redirect('/')

def login(request):
    check = User.objects.login(
        request.POST['email'],
        request.POST['password']
    )

    if not check["valid"]:
        for error in check["errors"]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/")

    else:
        request.session["users_id"] = check["user"].id
        request.session["user_name"] = check["user"].name
        messages.add_message(request, messages.SUCCESS, "Login Successful!! Welcome, " "{}".format(check["user"].username))
        return redirect('/dashboard')

def dashboard(request):

    data = {
        'check': None,
        'somevariable': None,
        'user': None,
        'order': None
    }
    data['check'] = User.objects.all()
    data['somevariable'] = Message.objects.all()
    data['user'] = request.session['user_name']
    data['order'] = Message.objects.order_by('-id')
        
    
    return render(request, 'thewall_app/dashboard.html', data, id)

def test(request):
    data = {
        'l': None,
        'check': None,
        'somevariable': None,
        'user': None,
        'order': None
    }

    data['check'] = User.objects.all()
    data['somevariable'] = Message.objects.all()
    data['user'] = request.session['user_name']
    data['order'] = Message.objects.order_by('-id')
    
    l = []
    users = User.objects.order_by('-id')
    for x in users:
        l.append(x.name)

    data['l'] = l
    

    return render(request, 'thewall_app/test.html', data)

def home(request):
    return redirect('/')

def message(request):
    check = Message.objects.make(
        request.POST['message'],
        request.session['users_id']
    )
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def comment(request, id):
    # comment_id = request.session['comment_id']
    Comment.objects.make_comment(
        request.POST['comment'],
        request.session['users_id'],
        id
    )

    
    
    return redirect('/dashboard')