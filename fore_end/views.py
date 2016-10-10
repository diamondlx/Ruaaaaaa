from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from backend import api

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def submit_user_info(request):
    dic = request.POST.dict()
    api.set_user_information(dic)
    print "registered"
    return render(request, 'login.html')