from django.shortcuts import render
from .models import Project, NextMonth
from form.models import Form

# Create your views here.
def index(request):
    projects = Project.objects.all()
    nextmonths = NextMonth.objects.all()
    forms = Form.objects.all()
    
    return render(request, 'index.html', {'projects': projects, 'nextmonths': nextmonths, 'forms': forms})