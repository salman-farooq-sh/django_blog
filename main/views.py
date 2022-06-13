from django.views.generic import ListView, DetailView

from .models import BlogPost


class HomePageView(ListView):
    def get_queryset(self):
        return BlogPost.objects.order_by('-publication_date')


class PostDetailView(DetailView):
    model = BlogPost
