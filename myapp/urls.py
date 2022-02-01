from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from bbs.views import index, detail

app_name = 'bbs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('<int:id>/', detail, name='detail')
]
