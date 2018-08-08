"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^list-tweets$', views.list_tweets),
    url(r'^add-tweets$', views.add_tweets),
    url(r'^signup$', views.signup),
    url(r'^login-page$', views.login_page),
    url(r'^logout-page$', views.logout_page),
    url(r'^update-tweet/(?P<tweet_id>\d+)$', views.update_tweet),
    url(r'^delete-tweet/(?P<tweet_id>\d+)$', views.delete_tweet)
]
