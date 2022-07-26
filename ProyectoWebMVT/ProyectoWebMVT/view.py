from datetime import datetime
from turtle import ht
from unittest import loader
from django.template import Template,Context
from django.http import HttpResponse
from django.shortcuts  import render
from django.template import loader 
from django.shortcuts import render


def Index(request):
    return render(request,"index.html",{}) 


def Integreantes(request):

    integrantes=['Piero Sayas','Leandro Luigui','Oscar Reyes','Jose Chavez']
    return render(request,"integrantes.html",{"integrantes":integrantes})

def Saludo(request):
    mensaje="Buen dia, le saluda los integrantes del grupo"
    return render(request,"saludo.html",{"mensaje":mensaje})
    