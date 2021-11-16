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

#Views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
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
        
        #Cuando se accede a la pagina del login, si el usuario ya está logueado, se lo redirige a la pagina de los movimientos
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

class PedidoVentaList(ListView):
    model = PedidoVenta
    template_name = 'base.html'