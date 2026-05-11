from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tube:category", kwargs={"slug": self.slug})


class Video(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    filename = models.CharField(
        max_length=255,
        blank=True,
        help_text="Filename only, e.g. getting-started.mp4 — file must be uploaded to the videos directory on the server. Leave blank if using a YouTube URL.",
    )
    youtube_url = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube video URL (e.g. https://www.youtube.com/watch?v=... or https://youtu.be/...). If set, the YouTube player and thumbnail are used automatically.",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos",
    )
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
    )
    order = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ["order", "-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tube:detail", kwargs={"slug": self.slug})

    # ── YouTube helpers (mirrors ebuilder blog pattern exactly) ───────────────

    def get_youtube_video_id(self):
        """Extract YouTube video ID from URL."""
        if not self.youtube_url:
            return None
        if "youtu.be" in self.youtube_url:
            return self.youtube_url.split("/")[-1]
        elif "v=" in self.youtube_url:
            return self.youtube_url.split("v=")[1].split("&")[0]
        return None

    def get_youtube_embed_url(self):
        """Return the YouTube embed URL, or None if not a YouTube video."""
        video_id = self.get_youtube_video_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    def get_youtube_thumbnail_url(self):
        """Return the YouTube-hosted thumbnail URL, or None if not a YouTube video."""
        video_id = self.get_youtube_video_id()
        if video_id:
            return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        return None
