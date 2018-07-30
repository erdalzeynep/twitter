# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

from app.models import Tweet


def home(req):
    return redirect('/list-tweets')


def list_tweets(request):
    tweet_list = Tweet.objects.all()

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
            return render(request, 'app/add-tweets.html')


    else:
        return render(request, 'app/add-tweets.html')

def update_tweet(request):
    return HttpResponse("Updating Tweet")
