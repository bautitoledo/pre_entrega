from django.urls import path
from AppFrailoni.views import *



urlpatterns = [
    path("producto/", producto, name= "producto"),
    path("proveedores/", proveedores, name= "proveedores"),
    path("cliente/", cliente, name= "cliente"),
    path("inicio/", inicio, name= "inicio"),
    path("busquedadedatos/", busquedadedatos, name= "busquedadedatos"),
    path("busqueda/", busqueda, name= "busqueda"),
    


]

