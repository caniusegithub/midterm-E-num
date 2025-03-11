from django.shortcuts import render

# Create your views here.

from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-dateUpdated')
    return render(request, 'wiki/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id) 
    return render(request, 'wiki/article_detail.html', {'article': article})