from django.shortcuts import render
from datetime import date
from django.http import Http404
# from django.http import HttpResponse

POSTS = [
    {"id":1,"titulo":"Mi primer post", "autor":"Gus","fecha":date(2026,11,26),"publicado":True,"contenido":"rutas,vistas y templates"},
    {"id":2,"titulo":"Aprerendiendo Django", "autor":"Benja","fecha":date(2026,10,20),"publicado":False,"contenido":"rutas,vistas y templates"},
    {"id":3,"titulo":"Mi primer post", "autor":"Gus","fecha":date(2026,11,26),"publicado":True,"contenido":"rutas,vistas y templates"},
    {"id":4,"titulo":"Mi primer post", "autor":"Gus","fecha":date(2026,11,26),"publicado":True,"contenido":"rutas,vistas y templates"},
]

def inicio(request):

    return render(request, "posts/inicio.html")

def listar_posts(request):

    return render(request, "posts/lista_posts.html", {"posts": POSTS})

def detalle_post(request, post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return render(request, "posts/detalle_post.html", {"post": post})
    raise Http404("El post no exite")

def contacto(request):
    return render(request, "posts/contacto.html")

def acerca_de(request):
    autor = {
        "nombre":"Gus",
        "bio":"Desarrollador python ",
        "especialidad":"Django"
    }
    return render(request,"posts/acerca_de.html",{"autor":autor})