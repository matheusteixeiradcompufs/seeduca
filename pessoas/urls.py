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
    'aluno/boletim/situacao/api/v1',
    views.SituacaoViewSet,
    basename='aluno-boletim-situacao-api',
)
pessoas_api_v1_router.register(
    'aluno/boletim/agenda/api/v1',
    views.AgendaRecadosViewSet,
    basename='aluno-agenda-api',
)
pessoas_api_v1_router.register(
    'aluno/boletim/agenda/recado/api/v1',
    views.RecadoViewSet,
    basename='aluno-agenda-recado-api',
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
    'transporte/api/v1',
    views.TransporteViewSet,
    basename='transporte-api',
)
pessoas_api_v1_router.register(
    'transporte/telefone/api/v1',
    views.TelefoneTransporteViewSet,
    basename='transporte-telefone-api',
)

pessoas_api_v1_router.register(
    'usuario/api/v1',
    views.UsuarioViewSet,
    basename='usuario-api',
)
pessoas_api_v1_router.register(
    'usuario/grupo/api/v1',
    views.GrupoViewSet,
    basename='usuario-grupo-api',
)

pessoas_api_v1_router.register(
    'funcionario/api/v1',
    views.FuncionarioViewSet,
    basename='funcionario-api',
)

urlpatterns = [
    path('', include(pessoas_api_v1_router.urls)),
    path('me/', views.GetMe.as_view(), name='get_me'),
    path('me/aluno/', views.GetMeAluno.as_view(), name='get_me_aluno'),
    path('reset-password/', views.ResetPasswordAPIView.as_view(), name='reset_password_request'),
    path('decode-token/', views.DecodeTokenAPIView.as_view(), name='decode_token'),
    path('agendasdisciplinas/', views.AgendaDisciplinas.as_view(), name='agendas_disciplinas'),
]