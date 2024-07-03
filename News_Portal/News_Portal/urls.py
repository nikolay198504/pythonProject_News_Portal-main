

from django.contrib import admin
from django.urls import path, include
from News.views import trigger_error  # Импортируем trigger_error из приложения News


urlpatterns = [
    path("admin/", admin.site.urls),
    #path('pages/', include('django.contrib.flatpages.urls')),
    #path('posts/', include('News.urls')),
    path('news/', include('News.urls')),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('trigger-error/', trigger_error),  # Маршрут для вызова ошибки



]


