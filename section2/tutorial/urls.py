from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from restaurantapi.views import UserViewSet, GroupViewSet
from restaurantapi.views import MenuViewSet, MenuItemViewSet
from restaurantapi.views import AvailableMenuList, AvailableMenuDetail

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
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^available_menus/$', AvailableMenuList.as_view()),
    url(r'^available_menus/(?P<pk>[0-9]+)/$', AvailableMenuDetail.as_view()),
)
