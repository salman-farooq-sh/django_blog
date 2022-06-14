from django.urls import path

from .views import HomePageView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
