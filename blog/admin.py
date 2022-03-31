from django.contrib import admin

from .models import Post, Author, Tag , Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","date" ,"author",)
    list_filter = ("author","date" , "tag",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name" , "email")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name","text","email","post")

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)