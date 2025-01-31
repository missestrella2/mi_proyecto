from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer

# este enfoque de APIVIEW es apropiado si quiero solo cargar usuarios
# si deseo un CRUD completo me conviene usar ModelViewSet

# class UsuarioCreateView(APIView):
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Usuario creado con éxito", "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import UsuarioSerializer

# Vista para gestionar usuarios con CRUD completo
class UsuarioViewSet(ModelViewSet):
    """
    API para gestionar usuarios. Permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



from django.shortcuts import render

# Esta vista renderiza la plantilla home.html y devuelve la respuesta.
def home(request):
    return render(request, 'home.html')


