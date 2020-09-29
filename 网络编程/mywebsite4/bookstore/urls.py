from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path(r'add', views.add_book),
    path(r'', views.index),
    path(r'add', views.new_book),
    path(r'list_all', views.list_book),
    path(r'filter_book', views.filter_book),
    path(r'one2one', views.one2one),
]