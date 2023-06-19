from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


def es_administrador(user):
    return user.is_authenticated and user.username == 'kamy' and user.is_superuser

@user_passes_test(es_administrador)
def vista_restringida(request):
    # Verificar que el usuario sea un administrador
    if not request.user.is_superuser:
        # Si el usuario no es un administrador, redirigir a una página de acceso denegado o mostrar un mensaje de error
        return HttpResponse("Acceso denegado. Solo los administradores pueden ver esta página.")

    # Código adicional específico para la vista restringida para el administrador
    # ...

    # Retornar la respuesta de la vista
    return HttpResponse("Bienvenido, administrador.")


def solo_administrador_required(view_func):
    actual_decorator = user_passes_test(es_administrador)
    
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

