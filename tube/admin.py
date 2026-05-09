from django.contrib import admin
from .models import Category, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published", "created")
    list_filter = ("category", "published")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "category",
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
