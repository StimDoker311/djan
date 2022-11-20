from django import template
from django.db.models import Count, Q

from news.models import Category, News

register = template.Library()


@register.simple_tag(name= 'get_list_categories')
def get_categories():
    return  Category.objects.all()



@register.inclusion_tag('news/list_categories.html')
def show_categoris():
    categories = Category.objects.annotate(cnt = Count('news', filter = Q(news__is_publiched = True))).filter(cnt__gt=0)
    return {"categories": categories}