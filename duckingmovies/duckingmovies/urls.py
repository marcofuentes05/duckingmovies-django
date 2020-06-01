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
from rest_framework_jwt.views import (obtain_jwt_token ,refresh_jwt_token)
from rest_framework import routers

from actors.views import ActorViewSet
from awards.views import AwardViewSet
from directors.views import DirectorViewSet
from genres.views import GenreViewSet
from movies.views import MovieViewSet
from series.views import SerieViewSet
from usuarios.views import UserViewSet
from comments.views import GameCommentViewSet, MovieCommentViewSet, SerieCommentViewSet
from consoles.views import ConsoleViewSet
from developers.views import DeveloperViewSet
from movie_producers.views import MovieProducerViewSet
from videogames.views import VideogameViewSet

from init import create_initial_data


router = routers.DefaultRouter()

router.register(r'actors', ActorViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'genres',GenreViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'series', SerieViewSet)
router.register(r'users', UserViewSet)
router.register(r'game-comments', GameCommentViewSet)
router.register(r'movie-comments', MovieCommentViewSet)
router.register(r'serie-comments', SerieCommentViewSet)
router.register(r'consoles', ConsoleViewSet)
router.register(r'developers', DeveloperViewSet)
router.register(r'movie-producers', MovieProducerViewSet)
router.register(r'videogames', VideogameViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^admin/initial-data/', create_initial_data),
]
