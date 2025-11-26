from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from core.views import PersonagemViewSet, ObraViewSet, HabilidadeViewSet, AtorViewSet, RelacionamentoViewSet


from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API de RPG",
      default_version='v1',
      description="Documentação completa da API de Personagens e Obras",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@meurpg.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'personagens', PersonagemViewSet)
router.register(r'obras', ObraViewSet)
router.register(r'habilidades', HabilidadeViewSet)
router.register(r'atores', AtorViewSet)
router.register(r'relacionamentos', RelacionamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redocf'),
]