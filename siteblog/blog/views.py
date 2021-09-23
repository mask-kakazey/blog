from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Photo Blog'
        return context


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__title=self.kwargs['title'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(title=self.kwargs['title'])
        return context


def index(request):
    return render(request, 'blog/index.html')


def get_category(request):
    return render(request, 'blog/category.html')


def get_post(request, slug):
    return render(request, 'blog/index.html')

