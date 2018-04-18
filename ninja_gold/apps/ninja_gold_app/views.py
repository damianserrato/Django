# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, "ninja_gold_app/index.html")

def process(request):
    import random
    if request.POST['place'] == "farm":
        request.session['randnum'] = random.randrange(10, 21)
        something = "Earned " + str(request.session['randnum']) + " golds from the farm!!"
    elif request.POST['place'] == "cave":
        request.session['randnum'] = random.randrange(5, 11)
        something = "Earned " + str(request.session['randnum']) + " golds from the cave!!"
    elif request.POST['place'] == "house":
        request.session['randnum'] = random.randrange(2, 6)
        something = "Earned " + str(request.session['randnum']) + " golds from the house!!"
    elif request.POST['place'] == "casino":
        num = random.randrange(1, 3)
        if num == 1:
            request.session['randnum'] = random.randrange(0, 51)
            something = "Entered a casino and earned " + str(request.session['randnum']) + " golds!!"
        else:
            request.session['randnum'] = random.randrange(-51, 0)
            

    if 'sum' not in request.session:
        request.session['sum'] = 0
    else:
        request.session['sum'] += request.session['randnum']

    
    if request.session['randnum'] < 0:
        request.session['randnum'] = request.session['randnum'] * -1
        something = "Entered a casino and lost " + str(request.session['randnum']) + " golds... ouch!!"
    

    if 'log' not in request.session:
        request.session['log'] = []
    else:
        request.session['log'].append(something)



    
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')