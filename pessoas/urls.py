from django.urls import include, path
from rest_framework.routers import SimpleRouter

from pessoas import views
from pessoas.views import GetMe

app_name = 'pessoas'

pessoas_api_v1_router = SimpleRouter()

pessoas_api_v1_router.register(
    'telefone/api/v1',
    views.TelefonePessoaViewSet,
    basename='telefone-api',
)
pessoas_api_v1_router.register(
    'email/api/v1',
    views.EmailPessoaViewSet,
    basename='email-api',
)
pessoas_api_v1_router.register(
    'aluno/api/v1',
    views.AlunoViewSet,
    basename='aluno-api',
)
pessoas_api_v1_router.register(
    'aluno/responsavel/api/v1',
    views.ResponsavelViewSet,
    basename='aluno-responsavel-api',
)
pessoas_api_v1_router.register(
    'aluno/boletim/api/v1',
    views.BoletimViewSet,
    basename='aluno-boletim-api',
)
pessoas_api_v1_router.register(
    'aluno/boletim/avaliacao/api/v1',
    views.AvaliacaoViewSet,
    basename='aluno-boletim-avaliacao-api',
)
pessoas_api_v1_router.register(
    'aluno/boletim/media/api/v1',
    views.MediaViewSet,
    basename='aluno-boletim-media-api',
)
pessoas_api_v1_router.register(
    'aluno/frequencia/api/v1',
    views.FrequenciaViewSet,
    basename='aluno-frequencia-api',
)
pessoas_api_v1_router.register(
    'aluno/frequencia/dialetivo/api/v1',
    views.DiaLetivoViewSet,
    basename='aluno-frequencia-dialetivo-api',
)
pessoas_api_v1_router.register(
    'aluno/transporte/api/v1',
    views.TransporteViewSet,
    basename='aluno-transporte-api',
)
pessoas_api_v1_router.register(
    'aluno/transporte/telefone/api/v1',
    views.TelefoneTransporteViewSet,
    basename='aluno-transporte-telefone-api',
)

pessoas_api_v1_router.register(
    'funcionario/api/v1',
    views.FuncionarioViewSet,
    basename='funcionario-api',
)

urlpatterns = [
    path('', include(pessoas_api_v1_router.urls)),
    path('me', GetMe.as_view(), name='get_me'),
]