from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting_page"),
    path("posts", views.Posts.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail-page"),
    path("read_later",views.ReadPost.as_view(),name="read_later")
]