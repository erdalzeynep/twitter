# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(req):
    context={}
   return render(request,  'app/index.html',context)

def list_tweets(request,author)
    return HttpResponse("You are looking %s user's tweet list" %author)

def add_tweet(request,author,content)
    return  HttpResponse("You added a new tweet : %s" %content)
