from django.urls import path
from .views import home
#from .views import UsuarioCreateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, home

# Creamos el enrutador para manejar las rutas automáticamente
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)  # /api/usuarios/

urlpatterns = [

    #path('crear-usuario/', UsuarioCreateView.as_view(), name='crear_usuario'),
    path('', home, name='home'),  # Página principal
     path('', include(router.urls)),  # Genera automáticamente las rutas de la AP
]



urlpatterns = [
    path('', include(router.urls)),  # Genera automáticamente las rutas de la API
    path('home/', home, name='home'),  # Página principal
]
