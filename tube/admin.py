from django.contrib import admin
from django.db import models
from .models import Category, Video
from tinymce.widgets import TinyMCE



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "category", "published", "created")
    list_editable = ("order",)
    list_filter = ("category", "published")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "-created")
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "category",
                    "order",
                    "published",
                )
            },
        ),
        (
            "Video Source",
            {
                "description": "Provide either a server filename OR a YouTube URL — not both.",
                "fields": (
                    "filename",
                    "youtube_url",
                    "thumbnail",
                ),
            },
        ),
    )


