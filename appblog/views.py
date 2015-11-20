from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Entrada


class IndexView(TemplateView):

    template_name = 'index.html'


class EntradaDetailView(DetailView):

    template_name = 'post.html'
    model = Entrada


def about(request):
    return render(request, 'about.html')


class noticia(ListView):
    model = Entrada
    paginate_by = 5
    template_name = 'noticias.html'

def inicio():
    pass
