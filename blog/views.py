from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'team': 'the Djangoblog team'})

def contact(request):
    return render(request, 'blog/contact.html', {
        'content': 'You can reach the Djangoblog team here.'
    })