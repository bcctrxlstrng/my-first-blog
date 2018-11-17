from django.shortcuts import render
from django.utils import timezone
from .models import Post # the . is for current directory or current application

# to take actual blog posts from the Post model, we use QuerySet

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})