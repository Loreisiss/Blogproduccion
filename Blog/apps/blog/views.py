from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    post = Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre='Home'))
    return render(request,'index.html',{'post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado=True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains=queryset)).distinct()
    paginator = Paginator(post,2)
    page = request.GET.get('page')
    post= paginator.get_page(page)
    return render(request,'generales.html',{'post':post})

def programa(request):
    post =Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre='Programacion'))
    return render(request,'programacion.html',{'post':post})

def contacto(request):
    post = Post.objects.filter(estado=True,categoria=Categoria.objects.get(nombre='Contacto'))
    return render(request,'contacto.html',{'post':post})

def detallespost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'post.html',{'detalle_post':post})