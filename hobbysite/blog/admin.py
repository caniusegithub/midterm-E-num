from django.contrib import admin

# Register your models here.

from .models import Post, PostCategory

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

class PostAdmin(admin.ModelAdmin):
    model = Post

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)