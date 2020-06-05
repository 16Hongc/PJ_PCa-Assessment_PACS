
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # 현재폴더(pca)에 있는 views.py폴더의 index함수를 실행

]
