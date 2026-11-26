# from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):

    return HttpResponse("Pagina inicio posts en construccion!!!")


def listar_posts(request):

    return HttpResponse("Pagina de listar los posts en construccion")

