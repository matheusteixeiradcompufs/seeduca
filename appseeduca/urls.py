from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from appseeduca import settings

urlpatterns = [
    # URL para a documentação administrativa
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # URL para o painel administrativo
    path('admin/', admin.site.urls),
    # URLs da aplicação 'escolas'
    path('escolas/', include('escolas.urls')),
    # URLs da aplicação 'pessoas'
    path('pessoas/', include('pessoas.urls')),
    # URL para obtenção de tokens de acesso JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL para atualização de tokens de acesso JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # URL para verificação de tokens de acesso JWT
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Adicionando URLs para servir arquivos de mídia em desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adicionando URLs para servir arquivos estáticos em desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
