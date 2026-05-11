from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from tube.models import Video, Category



class VideoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Video.objects.filter(published=True).select_related("category")

    def lastmod(self, obj):
        return obj.created

    def location(self, obj):
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return ["tube:list"]

    def location(self, item):
        return reverse(item)