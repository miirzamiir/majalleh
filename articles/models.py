from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from ckeditor.fields import RichTextField
from django.db.models.deletion import DO_NOTHING
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    photo = models.ImageField(null=True, blank=True, upload_to='article/')
    summary = models.CharField(max_length=400, blank=True)
    text = RichTextField(blank=True, null=True)
    tags = models.CharField(blank=True, max_length=250)
    category = models.ForeignKey(Category, on_delete=DO_NOTHING)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

    @classmethod
    def tag_box(cls):
        tag_box = []
        i = 0
        for art in Article.objects.order_by('-date').all()[:10]:
            if tag_box.__len__() > 12:
                break
            else:
                tag_box.extend(art.tags.split())
        tag_box = list(dict.fromkeys(tag_box))
        return tag_box

    @classmethod
    def slider(cls):
        slider = []
        for article in Article.objects.order_by('-date').all()[:3]:
            slider.append(article.photo.url)
        return slider
