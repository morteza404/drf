from .models import Article
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "content",
        "published_at",
        "created_at",
        "updated_at",
        "status",
    )
    list_filter = ("status", "created_at", "published_at", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
