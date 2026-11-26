from django.shortcuts import render
from datetime import date
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