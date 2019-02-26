from django.shortcuts import render 
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html', {'title': about})

def imSoHappy(request):
    return HttpResponse('<h1>Hey, I am Nick!</h1>')
