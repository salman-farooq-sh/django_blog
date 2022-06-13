from django.urls import path

from .views import HomePageView, PostDetailView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]