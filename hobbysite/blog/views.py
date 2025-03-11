from django.shortcuts import render

# Create your views here.

from .models import Post

def article_list(request):
    articles = Post.objects.all().order_by('-dateUpdated')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Post.objects.get(id=article_id) 
    return render(request, 'blog/article_detail.html', {'article': article})