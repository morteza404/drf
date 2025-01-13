from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"
        verbose_name = "article"
        verbose_name_plural = "articles"
        ordering = ["-created_at"]
