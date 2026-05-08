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
        help_text="Filename only, e.g. getting-started.mp4 — file must be uploaded to the videos directory on the server.",
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

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tube:detail", kwargs={"slug": self.slug})
