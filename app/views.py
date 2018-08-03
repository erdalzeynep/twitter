# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
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
