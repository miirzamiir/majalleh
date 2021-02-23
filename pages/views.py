from django.shortcuts import render
from articles.models import Article, Category


# Create your views here.


def index(request):

    context = {
        'articles': Article.objects.order_by('-date').all()[:10],
        'categories': Category.objects.order_by('name').all(),
        'tag_box': Article.tag_box(),
        'slider': Article.slider()

    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'categories': Category.objects.order_by('name').all()
    }
    return render(request, 'pages/about.html', context)
