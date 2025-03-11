from django.contrib import admin

# Register your models here.

from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    model = Article

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)