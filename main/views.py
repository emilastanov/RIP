from django.shortcuts import render, get_object_or_404
from .models import Main
from .db import db

def main(request):
    return render(request,'main/main.html', {'data': {'name': request.GET.get('name'), 'articles': Main.objects.all()}})

def imgPage(request):
    return render(request, 'main/images.html', {'data': {'name': request.GET.get('name')}})

def article(request,id,slug):
    article = get_object_or_404(Main, id=id, slug=slug)

    database = db(
        dbname='rip_lab4',
        password='1'
    )
    if request.GET.get('name') is not None and request.GET.get('text') is not None and request.GET.get('post') is not None:
        database.insert(
            'Comments',
            user=request.GET.get('name'),
            text=request.GET.get('text'),
            post=request.GET.get('post')
        )


    return render(request, "main/detail.html", context={'article': article, 'comments': database.get('Comments', post = slug)})