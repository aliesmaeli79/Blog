import datetime
from builtins import str
from datetime import datetime
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView ,ListView , DetailView

from django.http import HttpResponseRedirect
from django.views import View
from .models import Post
from .forms import FormsComment


class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        context = super().get_queryset()
        latest_post = context[:3]
        return latest_post


class Posts(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"
    ordering = ["date"]


class PostDetail(View):

    def is_saved_post(self,request,post_id):
        stored_post = request.session.get("stored_posts")
        if stored_post is not None :
            is_saved_post = post_id in stored_post
        else:
            is_saved_post = False
        return is_saved_post

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        comment = post.comments.all().order_by("-id")
        context = {
            "post":post,
            "comments":comment,
            "post_tags" : post.tag.all(),
            "comment_form": FormsComment(),
            "saved_post": self.is_saved_post(request,post.id)
        }
        return render(request,"blog/post-detail.html", context)

    def post(self,request,slug):
        form = FormsComment(request.POST)
        post = Post.objects.get(slug=slug)
        comment = post.comments.all().order_by("-id")
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page" ,args=[slug] ))

        context = {
            "post": post,
            "comments": comment,
            "post_tags": post.tag.all(),
            "comment_form": form,
            "saved_post": self.is_saved_post(request, post.id)
        }
        return render(request,"blog/post-detail.html", context)



class ReadPost(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")

        context = {}
        if stored_posts is None or len(stored_posts)==0 :
            context["posts"] = []
            context["has_post"]=False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context["posts"] = posts
            context["has_post"]=True

        return render(request,"blog/stored-posts.html",context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None :
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts :
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")









