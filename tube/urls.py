from django.urls import path
from . import views

app_name = "tube"

urlpatterns = [
    path("", views.VideoListView.as_view(), name="list"),
    path("category/<slug:slug>/", views.CategoryView.as_view(), name="category"),
    path("<slug:slug>/", views.VideoDetailView.as_view(), name="detail"),
]
