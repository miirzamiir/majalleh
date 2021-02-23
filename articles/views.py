from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Category
from django.core.files.storage import FileSystemStorage
from accounts.models import Profile
# Create your views here.


def single_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    profile = Profile.objects.filter(user=article.author).first()
    tags = article.tags.split()
    tag_box = Article.tag_box()
    context = {
        'article': article,
        'profile': profile,
        'categories': Category.objects.order_by('name').all(),
        'tags': tags,
        'tag_box': tag_box,
        'slider': Article.slider()

    }

    return render(request, 'articles/single_article.html', context)


def new_article(request):
    if request.user.is_authenticated:
        context = {
            'categories': Category.objects.order_by('name').all()
        }
        if request.method == 'GET':
            return render(request, 'articles/new_article.html', context)

        elif request.method == 'POST':
            photo = request.FILES['pic']
            title = request.POST['title']
            summary = request.POST['summary']
            tags = request.POST['tags']
            category = get_object_or_404(
                Category, name=request.POST['category'])
            text = request.POST['text']

            img_name = 'media/article/logo.png'
            if photo != None:
                fs = FileSystemStorage()
                img_name = fs.save(photo.name, photo)

            article = Article(author=request.user, title=title, summary=summary,
                              tags=tags, category=category, text=text, photo=img_name)

            article.save()
            return redirect('dashboard')

    return redirect('index')


def full_width(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    context = {
        'article': article,
        'profile': get_object_or_404(Profile, user=article.author),
        'categories': Category.objects.order_by('name').all(),
        'tags': article.tags.split(),

    }
    return render(request, 'articles/full_width.html', context)
