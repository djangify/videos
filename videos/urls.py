from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from videos.sitemaps import VideoSitemap, CategorySitemap, StaticSitemap

sitemaps = {
    "videos": VideoSitemap,
    "categories": CategorySitemap,
    "static": StaticSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("ai.txt", TemplateView.as_view(template_name="ai.txt", content_type="text/plain")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("", include("tube.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)