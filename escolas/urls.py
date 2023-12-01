from django.urls import path, include
from rest_framework.routers import SimpleRouter

from escolas import views

app_name = 'escolas'

escola_api_v1_router = SimpleRouter()
escola_api_v1_router.register(
    'api/v1',
    views.EscolaViewSet,
    basename='escola-api',
)

urlpatterns = [
    path('', include(escola_api_v1_router.urls))
]