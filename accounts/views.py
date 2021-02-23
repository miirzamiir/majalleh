import os
from django.contrib.auth.models import User
from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseNotFound
from .models import Profile
from django.core.files.storage import FileSystemStorage
from articles.models import Category, Article


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            messages.error(request, 'رمزهای عبور با هم مطابقت ندارند!')
            return render(request, 'account/register.html')

        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'ایمیل مورد نظر قبلا استفاده شده است!')
                return render(request, 'account/register.html')

            else:
                if User.objects.filter(username=username).exists():
                    messages.error(
                        request, 'نام کاربری مورد نظر قبلا استفاده شده است!')
                    return render(request, 'account/register.html')

                else:
                    user = User(username=username, email=email,
                                is_active=True, is_staff=False)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'شما با موفقیت ثبت نام شدید!')
                    return render(request, 'account/register.html')

    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        context = {}

        if user:
            auth.login(request, user)
            profile = Profile.objects.filter(user=user).first()

            context = {
                'profile': profile,
            }
            return render(request, 'account/dashboard.html', context)
        else:
            messages.error(request, 'کاربری با این مشخصات پیدا نشد!')
            return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.filter(user=user).first()

        context = {
            'profile': profile,
            'categories': Category.objects.order_by('name').all(),
            'articles': Article.objects.filter(author=user).order_by('-date').all()
        }
        return render(request, 'account/dashboard.html', context)
    else:
        return redirect('index')


def edit_profile(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            user = request.user
            profile = Profile.objects.filter(user=user).first()
            context = {
                'profile': profile,
                'categories': Category.objects.order_by('name').all()

            }
            return render(request, 'account/edit_profile.html', context)

        elif request.method == 'POST':
            old_username = request.user.username
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            age = request.POST['age']
            bio = request.POST['bio']
            pic = request.FILES.get('pic')

            if (username == None) or (User.objects.filter(username=username).count() >= 1 and username != request.user.username):
                messages.error(request, 'نام کاربری مجاز نیست!')
                context = {
                    'categories': Category.objects.order_by('name').all()
                }
                return render(request, 'account/edit_profile.html', context)

            else:
                if (email == None) or (User.objects.filter(email=email).count() >= 1 and email != request.user.email):
                    messages.error(request, 'ایمیل مجاز نیست!')
                    context = {
                        'categories': Category.objects.order_by('name').all()
                    }
                    return render(request, 'account/edit_profile.html', context)

                else:

                    old_user = request.user

                    # Updating User table record.
                    User.objects.filter(username=old_username).update(
                        username=username, email=email, first_name=first_name, last_name=last_name)
                    user = User.objects.get(username=username)

                    # Updating Profile table record.
                    profile = Profile.objects.filter(user=old_user).first()
                    if profile:
                        if(pic != None):
                            fs = FileSystemStorage()
                            img_name = fs.save(pic.name, pic)
                            img_url = fs.url(img_name)
                        Profile.objects.filter(user=old_user).update(user=user, photo=img_name,
                                                                     phone=phone, age=age, bio=bio)
                    else:
                        new_profile = Profile(user=user, age=age,
                                              phone=phone, photo=pic, bio=bio)
                        new_profile.save()
                    return redirect('dashboard')
    else:
        return redirect('index')


def author(request, author):
    user = User.objects.filter(username=author).first()
    profile = Profile.objects.filter(user=user).first()
    articles = Article.objects.filter(author=user).order_by('date').all()
    context = {
        'profile': profile,
        'categories': Category.objects.order_by('name').all(),
        'slider': Article.slider(),
        'tag_box': Article.tag_box(),
        'articles': articles
    }
    return render(request, 'account/author.html', context)
