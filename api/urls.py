from django.urls import path
from .views import home
from .views import UsuarioCreateView

urlpatterns = [

    path('crear-usuario/', UsuarioCreateView.as_view(), name='crear_usuario'),
    path('', home, name='home'),  # Página principal
]


