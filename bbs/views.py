from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    post ={
        "title": "これはタイトルです",
        'players': ["勇者", "戦士", "魔法使い"],
        'articles': articles
    }
    return render(request, 'bbs/index.html', post)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'bbs/detail.html', {'article': article})

def create(request):
    article = Article(content='createメソッド', name="サトウ")
    article.save()
    
    articles = Article.objects.all()
    post ={
        "title": "これはタイトルです",
        'players': ["勇者", "戦士", "魔法使い"],
        'articles': articles
    }
    return render(request, 'bbs/index.html', post)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    articles = Article.objects.all()
    post ={
        "title": "これはタイトルです",
        'players': ["勇者", "戦士", "魔法使い"],
        'articles': articles,
    }
    return render(request, 'bbs/index.html', post)