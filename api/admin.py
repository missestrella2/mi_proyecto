from django.contrib import admin
from .models import Usuario  # Importá el modelo

admin.site.register(Usuario)  # Lo registramos en el panel de admin
