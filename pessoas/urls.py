from django.urls import include, path
from rest_framework.routers import SimpleRouter

from pessoas import views

app_name = 'pessoas'

pessoas_api_v1_router = SimpleRouter()
pessoas_api_v1_router.register(
    'aluno/api/v1',
    views.AlunoViewSet,
    basename='aluno-api',
)

pessoas_api_v1_router.register(
    'funcionario/api/v1',
    views.FuncionarioViewSet,
    basename='funcionario-api',
)

urlpatterns = [
    path('', include(pessoas_api_v1_router.urls)),
]