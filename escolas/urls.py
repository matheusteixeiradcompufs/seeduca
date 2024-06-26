from django.urls import path, include
from rest_framework.routers import SimpleRouter
from escolas import views

app_name = 'escolas'

# Criando um roteador para a API da escola
escola_api_v1_router = SimpleRouter()

# Registrando os endpoints da API da escola com seus respectivos viewsets
escola_api_v1_router.register(
    'api/v1',
    views.EscolaViewSet,
    basename='escola-api',
)
escola_api_v1_router.register(
    'telefone/api/v1',
    views.TelefoneEscolaViewSet,
    basename='escola-telefone-api',
)
escola_api_v1_router.register(
    'email/api/v1',
    views.EmailEscolaViewSet,
    basename='escola-email-api',
)
escola_api_v1_router.register(
    'disciplina/api/v1',
    views.DisciplinaViewSet,
    basename='escola-disciplina-api',
)
escola_api_v1_router.register(
    'mural/api/v1',
    views.MuralAvisosViewSet,
    basename='escola-mural-api',
)
escola_api_v1_router.register(
    'mural/aviso/api/v1',
    views.AvisoEscolaViewSet,
    basename='escola-mural-aviso-api',
)
escola_api_v1_router.register(
    'cardapio/api/v1',
    views.CardapioMerendaViewSet,
    basename='escola-cardapio-api',
)
escola_api_v1_router.register(
    'cardapio/item/api/v1',
    views.ItemCardapioMerendaViewSet,
    basename='escola-cardapio-item-api',
)
escola_api_v1_router.register(
    'sala/api/v1',
    views.SalaViewSet,
    basename='escola-sala-api',
)
escola_api_v1_router.register(
    'sala/turma/api/v1',
    views.TurmaViewSet,
    basename='escola-sala-turma-api',
)
escola_api_v1_router.register(
    'sala/turma/agenda/api/v1',
    views.AgendaEscolarViewSet,
    basename='escola-sala-turma-agenda-api',
)
escola_api_v1_router.register(
    'sala/turma/agenda/dia/api/v1',
    views.DiaAgendaViewSet,
    basename='escola-sala-turma-agenda-dia-api',
)
escola_api_v1_router.register(
    'sala/turma/agenda/dia/tarefa/api/v1',
    views.TarefaViewSet,
    basename='escola-sala-turma-agenda-dia-tarefa-api',
)
escola_api_v1_router.register(
    'sala/turma/agenda/dia/aviso/api/v1',
    views.AvisoViewSet,
    basename='escola-sala-turma-agenda-dia-aviso-api',
)

# Definindo as URLs da aplicação
urlpatterns = [
    path('', include(escola_api_v1_router.urls))
]
