from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def evenodd(request):
    dict={}
    if request.method == "POST":
        box = int(request.POST.get("box"))
        if box % 2 == 0:
            output = "Even Number"
        else:
            output = "Odd Number"
        
        dict={
            'output': output
        }
    return render(request, "evenodd.html", dict)