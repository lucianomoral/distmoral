"""distmoral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.main.views import IndexLogin, log_user_out, IndexLoginError, PedidoVentaList, ABM_General, PruebaDeAPIs, APIPrueba, ClientesAPI

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', IndexLogin.as_view(), name="indexLogin"),
    path('indexLoginError/',IndexLoginError.as_view(), name='indexLoginError'),
    path('logout/', log_user_out, name="logout"),
    path('listarPedidosVenta/', PedidoVentaList.as_view(), name='listarPedidosVenta'),
    path('listar/<modelo>/', ABM_General.as_view(), name='abm_general'),
    path('PruebaDeAPIs', PruebaDeAPIs.as_view(), name='PruebaDeAPIs'),
    path('APIPrueba', APIPrueba.as_view(), name='APIPrueba'),
    path('API/clientes', ClientesAPI.as_view(), name='ClientesAPI'),
]
