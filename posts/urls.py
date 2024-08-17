from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import Post

# Posts list
# Single post of blog
# Contact's section

urlpatterns = [
    path("", ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = "post_list.html",
        paginate_by = 8
    ), name="list"),

    path("<int:pk>/<slug:slug>/", DetailView.as_view(
        model = Post,
        template_name = "single_post.html"
    ), name="single"),

    path("contact/", post_views.contact, name="contact")
]

