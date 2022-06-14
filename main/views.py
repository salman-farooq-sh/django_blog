from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BlogPost


class HomePageView(ListView):
    def get_queryset(self):
        return BlogPost.objects.order_by('-publication_date')


class PostDetailView(DetailView):
    model = BlogPost


class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'author', 'publication_date', 'body']
    template_name = 'main/blogpost_create_form.html'


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'body']
    template_name = 'main/blogpost_update_form.html'


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('main:homepage')
