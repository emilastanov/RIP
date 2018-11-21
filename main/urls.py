from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.shortcuts import HttpResponseRedirect

app_name = "main"

urlpatterns = [
    path('',views.main),
    path('images', views.imgPage),
    re_path(r'(main/static/)', lambda request,arg: HttpResponseRedirect(request.path.replace("main/",""))),
    path('<int:id>/<slug:slug>/', views.article, name="article")
]
