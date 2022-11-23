from django.shortcuts import render
from .models import Project, Recommended, Comingsoon

# Create your views here.
def index(request):
    projects = Project.objects.all()
    recommendeds = Recommended.objects.all()
    comingsoons = Comingsoon.objects.all()
    return render(request, 'index.html', {'projects': projects, 'recommendeds': recommendeds, 'comingsoons': comingsoons})