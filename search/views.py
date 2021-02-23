from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from articles.models import Article, Category
from accounts.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def search(request):
    q = request.GET['q']
    page = request.GET['page_number']

    # fetching articles
    articles = Article.objects.order_by('-date').filter(
        Q(title__icontains=q) | Q(summary__icontains=q))

    paginator = Paginator(articles, 2)
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'categories': Category.objects.order_by('name').all(),
        'slider': Article.slider(),
        'tag_box': Article.tag_box(),
        'q': q
    }
    return render(request, 'search/search.html', context)


def tags(request):
    tag = request.GET['tag']
    page = request.GET['page_number']

    # fetching articles
    articles = Article.objects.order_by('-date').filter(
        tags__icontains=tag)

    paginator = Paginator(articles, 2)
    paged_articles = paginator.get_page(page)
    context = {
        'articles': paged_articles,
        'categories': Category.objects.order_by('name').all(),
        'slider': Article.slider(),
        'tag_box': Article.tag_box(),
        'q': tag
    }
    return render(request, 'search/tags.html', context)


def category(request):
    q = request.GET['category']
    page = request.GET['page_number']

    category = Category.objects.filter(name=q).first()
    articles = Article.objects.filter(category=category)

    paginator = Paginator(articles, 2)
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles,
        'categories': Category.objects.order_by('name').all(),
        'slider': Article.slider(),
        'tag_box': Article.tag_box(),
        'q': q
    }
    return render(request, 'search/category.html', context)
