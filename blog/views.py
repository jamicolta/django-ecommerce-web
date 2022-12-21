from django.shortcuts import render, get_object_or_404
from .models import Post
from main.models import Project
from form.models import Form

# Create your views here.
def render_about(request):
    return render(request, 'about.html')

def render_privacy(request):
    return render(request, 'privacy.html')

def render_post(request):
    posts = Post.objects.all()
    forms = Form.objects.all()
    return render(request, 'posts.html', {'posts': posts, 'forms': forms})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    projects = Project.objects.all()
    return render(request, 'post_detail.html', {'post': post, 'projects': projects})