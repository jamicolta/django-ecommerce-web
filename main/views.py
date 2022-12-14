from django.shortcuts import render
from .models import Project
from form.models import Form
# from django.core.paginator import Paginator
# from django.http import Http404

# Create your views here.
def index(request):
    projects = Project.objects.all()
    forms = Form.objects.all()
    # page = request.GET.get('page', 1)
    # try:
    #     paginator = Paginator(posts, 3)
    #     posts = paginator.page(page)
    # except:
    #     raise Http404
    return render(request, 'index.html', {'projects': projects, 'forms': forms
    #, 'paginator': paginator
    })