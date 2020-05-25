"""duckingmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from actors.views import ActorViewSet
from awards.views import AwardViewSet
from directors.views import DirectorViewSet
from genres.views import GenreViewSet
from movies.views import MovieViewSet
from series.views import SerieViewSet
from usuarios.views import UserViewSet


router = routers.DefaultRouter()

router.register(r'actors', ActorViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'genres',GenreViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'series', SerieViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))

]
