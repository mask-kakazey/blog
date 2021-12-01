from django import template

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_post_tpl.html')
def get_popular(cnt=5):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('blog/most_popular_tpl.html')
def most_popular():
    posts = Post.objects.order_by('-views')[:2]
    return {'posts': posts}
