from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from .models import NewsView

def news(request):
    news = NewsView.objects.order_by('-date')[:3]
    return render(request, 'news/home.html', {'news': news})
