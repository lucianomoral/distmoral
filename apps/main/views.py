#Functions
from typing import List
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, request
from django.core import serializers

#Views
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, TemplateView
#from django.contrib.auth import views as auth_views

#Models
#from django.contrib.auth.models import User
from .models import Cliente, ListaPrecio, ListaPrecioLinea, Producto, GrupoProducto, FamiliaProducto, PedidoVenta, PedidoVentaLinea

#Forms
#from .forms import MovimientoFinancieroForm, CuentaForm, CategoriaMovimientoFinancieroForm

#Otros
#from decimal import Decimal as D

# Create your views here.

class IndexLogin(TemplateView):
    template_name = 'indexLogin.html'

    def get(self, request):
        
        #Cuando se accede a la pagina del login, si el usuario ya está logueado, se lo redirige a la pagina de los pedidos de venta
        if request.user is None:
            return render(request, self.template_name)
        elif request.user.is_authenticated:
            return redirect('admin/')
        else:
            return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listarPedidosVenta/')
        else:
            return redirect('indexLoginError')

class IndexLoginError(TemplateView):
    template_name = 'indexLoginError.html'

def log_user_out(request):
    logout(request)
    return redirect('/')

@method_decorator(login_required(login_url='/'), name='dispatch')
class PedidoVentaList(ListView):
    model = PedidoVenta
    template_name = 'base.html'

@method_decorator(login_required(login_url='/'), name='dispatch')
class ABM_General(ListView):
    template_name = 'abmgeneral.html'

    model = ''

    modelos_permitidos = {
                            'Cliente': { 'titulo_pagina': 'Clientes' , 'modelo': Cliente},
                            'Producto': { 'titulo_pagina': 'Productos', 'modelo': Producto}, 
                            'GrupoProducto': { 'titulo_pagina': 'Grupos de Productos', 'modelo': GrupoProducto}, 
                            'FamiliaProducto': {'titulo_pagina': 'Familias de Productos', 'modelo': FamiliaProducto}
                            }

    def get_queryset(self):
        
        modelo_respuesta = ''

        if self.kwargs['modelo'] not in self.modelos_permitidos.keys():
            
            pass

        else:

            self.model = self.modelos_permitidos[self.kwargs['modelo']]['modelo']

            modelo_respuesta = serializers.serialize('json', self.model.objects.all())

            return modelo_respuesta

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        modelo_parametro = self.kwargs['modelo']

        if modelo_parametro not in self.modelos_permitidos.keys():
            
            context['titulo_pagina'] = 'No encontrado'

        else:

            #context['modelkeys'] = self.modelos_permitidos[modelo_parametro]['modelo']._meta.get_fields()

            context['titulo_pagina'] = 'Lista de ' + self.modelos_permitidos[modelo_parametro]['titulo_pagina']
        
        return context

# APIS - Nueva version
    
class PruebaDeAPIs(TemplateView):

    template_name = 'PruebaDeAPIs.html'


class APIPrueba(View):

    def get(self, request, *args, **kwargs):

        #Si se hace una request tipo ajax, entonces se devuelve el json con los registros de la pagina solicitada
        #if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        return JsonResponse({"data": "LARECONCHADETUMADRE"}, status = 200)

class ClientesAPI(View):

    def get(self, request, *args, **kwargs):

        #Si se hace una request tipo ajax, entonces se devuelve el json con los registros de la pagina solicitada
        #if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        return JsonResponse({"data": "LARECONCHADETUMADREFORRA"}, status = 200)
