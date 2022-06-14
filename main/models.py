from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_deleted_user),
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail', kwargs={'pk': self.pk})
