from django.urls import path
from .views import inicio, gatos, tarjetas, Formulario, Vision, Login, registrar, agregar_producto,modificar_producto, eliminar_producto, Venta,lista_productos 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('gatos/', gatos, name="gatos"),
    path('tarjetas/', tarjetas, name="tarjetas"),
    path('Formulario/', Formulario, name="Formulario"),
    path('Vision/', Vision, name="Vision"),
    path('Login/', Login, name="Login"),
    path('registrar/', registrar, name="registrar"),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<str:nombre>/', eliminar_producto, name='eliminar_producto'),
    path('modificar_producto/<str:nombre>/', modificar_producto, name='modificar_producto'),
    path('Venta/', Venta, name="Venta"),
]
