from django.shortcuts import render
from django.views.generic import ListView
from .models import Smoothie

def index(request):
    return render(request, 'smoothie/index.html')


class SmoothieListView(ListView):
    model = Smoothie
    template_name = 'smoothie/list.html'
    ordering = ['-date_created']
    context_object_name = 'smoothies'
    paginate_by = 6