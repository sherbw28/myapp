from ast import keyword
from http.client import HTTPResponse
from re import search
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm, ArticleForm

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()
    post ={
        "title": "これはタイトルです",
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', post)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'bbs/detail.html', {'article': article})

def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
            
    post ={
        "title": "これはタイトルです",
        'article': article
    }
    return render(request, 'bbs/detail.html', post)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    
    searchForm = SearchForm()
    articles = Article.objects.all()
    
    post ={
        "title": "これはタイトルです",
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', post)

def new(request):
    articleForm = ArticleForm()
    
    context = {
        'message': 'New Article',
        'articleForms': articleForm,
    }
    return render(request, 'bbs/new.html', context)

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message':'投稿の編集',
        'article':article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)
    
def update(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
        
        context = {
            'message':'これはタイトルです',
            'article':article
        }
    return render(request, 'bbs/detail.html', context)