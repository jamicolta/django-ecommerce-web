from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
def render_post(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(posts, 3)
        posts = paginator.page(page)
    except:
        raise Http404
    return render(request, 'posts.html', {'posts': posts, 'paginator': paginator})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def render_about(request):
    return render(request, 'about.html')