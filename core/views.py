from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto

from django.http import HttpResponse #formato que as paginas de erro do django funciona

from django.template import loader


def index(request):

    produtos =  Produto.objects.all()  #buscando todos os produtos, retorando uma lista

    context = {
        'Curso': 'Programação Web com Django',
        'produtos': produtos
        
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request,pk):
    #prod = Produto.objects.get(id=pk)  #busca um dado expecifico 

    prod =  get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')

    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404 )

#def error500(request, ex):
    template = loader.get_template('500.html')

    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=500 )