from django.conf.urls import url, include
from django.contrib import admin
from documents import views

urlpatterns = [
    url(r'^documents', views.uploadText, name='documents'),
    url(r'^get', views.getText, name='getText'),
]