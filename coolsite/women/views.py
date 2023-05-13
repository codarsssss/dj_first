from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить статью', 'url_name': 'add_page'},
            {'title': 'Обратная саязь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'}]


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


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    cat_slug = Category.objects.get(pk=post.cat_id).slug
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': cat_slug
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    cat_id = Category.objects.get(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat_id.pk)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'title': 'Главная страница',
               'cat_selected': cat_slug
    }

    return render(request, 'women/index.html', context=context)
