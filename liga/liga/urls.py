"""
URL configuration for liga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#urls.py de liga
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('gestion/', include('ligaApp.urls')),  # Incluir las URLs de tu aplicación
    path('', RedirectView.as_view(url='/gestion/', permanent=True)),  # Redirigir la raíz a /gestion/
]

