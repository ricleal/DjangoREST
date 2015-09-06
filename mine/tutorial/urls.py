"""tutorial URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from restaurantapi.views import UserViewSet, GroupViewSet,\
    MenuViewSet, MenuItemViewSet
from restaurantapi.views import AvailableMenuList, AvailableMenuDetail


# This will work for the rest api:
#     "user": "http://localhost:8000/user/",
#     "group": "http://localhost:8000/group/",
#     "menu": "http://localhost:8000/menu/",
#     "menuitem": "http://localhost:8000/menuitem/"
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'menuitem', MenuItemViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tutorial.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')),
                       url(r'^available_menus/$',
                           AvailableMenuList.as_view()),
                       url(r'^available_menus/(?P<pk>[0-9]+)/$',
                           AvailableMenuDetail.as_view()),
                       )
