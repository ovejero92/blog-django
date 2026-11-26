from django.urls import path
from posts.views import inicio, listar_posts

urlpatterns = [
    path("", inicio),
    path("listar", listar_posts),
]