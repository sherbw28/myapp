from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    post ={
        "title": "これはタイトルです",
        'players': ["勇者", "戦士", "魔法使い"]
    }
    return render(request, 'bbs/index.html', post)
