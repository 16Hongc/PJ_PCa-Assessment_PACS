
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index),  # 현재폴더(pca)에 있는 views.py폴더의 index함수를 실행
    path('', views.patient_list_view.get()),  # 현재폴더(pca)에 있는 views.py폴더의 index함수를 실행

]
