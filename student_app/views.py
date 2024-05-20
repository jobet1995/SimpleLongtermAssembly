"""
@description: Views for rendering the Student Page
@author: Jobet Casquejo
@last modified date: 5-19-2024
@last modified by: Jobet Casquejo
Modification Logs
Ver     Author              Date            Log
1.0     Jobet Casquejo      5-19-2024       Initial creation
"""
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def loginUser(request):
    return render(request, 'login.html')


def doLogin(request):
    username = request.get('username')
    password = request.get('password')

    print(username)
    print(password)
    print(request.user)

    if not (username and password):
        messages.error(request, "Username and Password don't match")
        return render(request, 'login.html')
    user = CustomUser.objects.filter(username=username,
                                     password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials')
        return render(request, 'login.html')

    login(request, user)
    print(request.user)

    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type == CustomUser.HOD:
        return redirect('admin_home/')

    return render(request, 'home.html')


def logoutUser(request):
    logoutUser(request)
    return HttpResponseRedirect('/')
