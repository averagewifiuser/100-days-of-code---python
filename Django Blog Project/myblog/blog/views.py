from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'title': 'Django Blog',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)