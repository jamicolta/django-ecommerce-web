from django.shortcuts import render
from .models import Project, NextMonth

# Create your views here.
def index(request):
    projects = Project.objects.all()
    nextmonths = NextMonth.objects.all()
    return render(request, 'index.html', {'projects': projects, 'nextmonths': nextmonths})