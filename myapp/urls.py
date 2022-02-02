from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from bbs.views import index, detail, create, delete, new, edit, update
from django.views.generic import RedirectView

app_name = 'bbs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', index, name="index"),
    path('bbs/<int:id>/', detail, name='detail'),
    path('', RedirectView.as_view(url='bbs/')),
    path('bbs/create/', create, name='create'),
    path('bbs/<int:id>/delete', delete, name='delete'),
    path('bbs/new/', new, name='new'),
    path('bbs/<int:id>/edit/', edit, name='edit'),
    path('bbs/<int:id>/update/', update, name='update'),
]
