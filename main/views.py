from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

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

