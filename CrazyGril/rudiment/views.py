from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext



# @login_required(login_url='/oauth/login/')
def rudiment(request):
    return render(request, "rudiment_content.html")


# @login_required(login_url='/oauth/login/')
def content(request):
    return render(request, "rudiment_content.html")


# @login_required(login_url='/oauth/login/')
def update_time_line(request):
    return render(request, "update_time_line.html")


# @login_required(login_url='/oauth/login/')
def project_log(request):
    return render(request, "update_time_line.html")

# @login_required(login_url='/oauth/login/')
def feedback(request):
    print "nimabio"
    return render(request, "feedback.html")
