from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('smoothies/', views.SmoothieListView.as_view(), name='smoothies-list'),
]