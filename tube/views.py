from django.views.generic import ListView, DetailView
from .models import Video, Category


class VideoListView(ListView):
    model = Video
    template_name = "tube/video_list.html"
    context_object_name = "videos"

    def get_queryset(self):
        return Video.objects.filter(published=True).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryView(ListView):
    model = Video
    template_name = "tube/category.html"
    context_object_name = "videos"

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs["slug"])
        return Video.objects.filter(
            category=self.category, published=True
        ).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


class VideoDetailView(DetailView):
    model = Video
    template_name = "tube/video_detail.html"
    context_object_name = "video"

    def get_queryset(self):
        return Video.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        if self.object.category:
            context["related_videos"] = Video.objects.filter(
                category=self.object.category, published=True
            ).exclude(id=self.object.id)[:6]
        return context
