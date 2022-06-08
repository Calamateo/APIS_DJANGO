"""ProyectoCCG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from ApisGenerate import views

schema_view = get_schema_view(
   openapi.Info(
      title="Conectar back con front",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dany.calamateo@gmail.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('OmniClass23', views.OmniClass23ViewSet)
router.register('OMC23Nivel1', views.OMC23Nivel1ViewSet)
router.register('OMC23Nivel2', views.OMC23Nivel2ViewSet)
router.register('OMC23Nivel3', views.OMC23Nivel3ViewSet)
router.register('OMC23Nivel4', views.OMC23Nivel4ViewSet)
router.register('OMC23Nivel5', views.OMC23Nivel5ViewSet)
router.register('OMC23Nivel6', views.OMC23Nivel6ViewSet)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('uniformat/', include('uniformat.urls')),
    path('', include('ProyectoCCGApp.urls')),   
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)