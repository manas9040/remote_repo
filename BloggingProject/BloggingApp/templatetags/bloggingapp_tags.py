from BloggingApp.models import Post
from django import template
from django.db.models import Count

register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('bloggingapp/latest_posts123.html')
def show_latest_posts(count):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return{'latest_posts':latest_posts}


@register.simple_tag
def get_most_commented_posts(count=3):
    most_commented_posts=Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return most_commented_posts