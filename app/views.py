# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from app.models import Tweet


def home(req):
    return redirect('/list-tweets')


def list_tweets(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    tweet_list = Tweet.objects.filter(author=username)

    context = {
        'tweets': tweet_list,
        'tweet_count': len(tweet_list)
    }
    return render(request, 'app/list-tweets.html', context)


def add_tweets(request):
    if request.method == 'POST':
        if request.POST.get('content') and request.POST.get('author'):
            tweet = Tweet()
            tweet.content = request.POST.get('content')
            tweet.author = request.POST.get('author')
            tweet.save()
            return redirect('/list-tweets')
    else:
        return render(request, 'app/add-tweets.html')


def update_tweet(request, tweet_id):
    if request.method == 'GET':
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        return render(request, 'app/update-tweet.html', {'tweet': tweet})
    else:
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        tweet.content = request.POST.get('content')
        tweet.author = request.POST.get('author')
        tweet.save()
        return redirect('/list-tweets')


def delete_tweet(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        tweet.delete()
        return redirect('/list-tweets')

    else:

        tweet = get_object_or_404(Tweet, pk=tweet_id)
        return render(request, 'app/delete-tweet.html', {'tweet': tweet})


def signup(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('email'):
            input_username = request.POST.get('username')
            input_password = request.POST.get('password')
            input_email = request.POST.get('email')
            User.objects.create_user(input_username, input_email, input_password)
            return redirect('/login-page')
    else:

        return render(request, 'app/signup.html')


def login_page(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            input_username = request.POST.get('username')
            input_password = request.POST.get('password')
            user = authenticate(request, username=input_username, password=input_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/list-tweets')
                else:
                    return HttpResponse("Disabled user")  # buraya girmiyor?
            else:

                return redirect('/signup')
    else:
        return render(request, 'app/login-page.html')


def logout_page(request):

    logout(request)
    return redirect('/login-page')
