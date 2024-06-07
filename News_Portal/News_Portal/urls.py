

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('pages/', include('django.contrib.flatpages.urls')),
    #path('posts/', include('News.urls')),
    path('news/', include('News.urls')),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),


]


