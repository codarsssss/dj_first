from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *





def index(request):
    posts = Women.objects.all()
    context = {'posts': posts,
               'title': 'Главная страница',
               'cat_selected': 0}

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Автоматизация')


# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('home', permanent=False)
#
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</1h>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статье с id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'title': 'Главная страница',
               'cat_selected': cat_id}

    return render(request, 'women/index.html', context=context)
