from django.urls import path
from posts.views import inicio, listar_posts, detalle_post, contacto, acerca_de

urlpatterns = [
    path("", inicio, name="inicio"),
    path("listar", listar_posts, name="lista_posts"),
    path("<int:post_id>", detalle_post, name="detalle_post"),
    path("contacto/", contacto, name="contacto"),
    path("acerca-de/", acerca_de, name="acerca_de"),
]

# /posts/1