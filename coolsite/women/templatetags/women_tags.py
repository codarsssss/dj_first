from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort, cat_selected):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


# @register.inclusion_tag('women/main_menu.html')
# def show_main_menu():
#     menu = [{'title': 'О сайте', 'url_name': 'about'},
#             {'title': 'Добавить статью', 'url_name': 'add_page'},
#             {'title': 'Обратная саязь', 'url_name': 'contact'},
#             {'title': 'Войти', 'url_name': 'login'}]
#
#     return {'menu': menu}
