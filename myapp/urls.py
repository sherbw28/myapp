from unicodedata import name
from django.contrib import admin
from django.urls import path
from bbs.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index")
]
