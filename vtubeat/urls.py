"""vtubeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from post import views as post_views

urlpatterns = [

    url(r'^$',post_views.index),
    url(r'^post/$',post_views.submit),
    url(r'^query/(?P<slug>[\w\-]+)/?$',post_views.fetch_query),
    url(r'^category/(?P<slug>[\w\-]+)/?$',post_views.fetch_category),
    url(r'^user/(?P<slug>[\w\-]+)/?$',post_views.fetch_user),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/',post_views.profile),
    url(r'^accounts/', include('allauth.urls')),
]
