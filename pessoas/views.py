from rest_framework import viewsets

from pessoas.models import Aluno, Funcionario, Responsavel, Boletim, Avaliacao, Frequencia, DiaLetivo, Transporte, \
    TelefonePessoa, EmailPessoa, TelefoneTransporte
from pessoas.permissions import AlunoPermission, FuncionarioPermission, ResponsavelPermission, BoletimPermission, \
    AvaliacaoPermission, FrequenciaPermission, DiaLetivoPermission, TransportePermission
from pessoas.serializers import AlunoSerializer, FuncionarioSerializer, ResponsavelSerializer, BoletimSerializer, \
    AvaliacaoSerializer, FrequenciaSerializer, DiaLetivoSerializer, TransporteSerializer, TelefonePessoaSerializer, \
    EmailPessoaSerializer, TelefoneTransporteSerializer


class TelefonePessoaViewSet(viewsets.ModelViewSet):
    queryset = TelefonePessoa.objects.all()
    serializer_class = TelefonePessoaSerializer
    permission_classes = [
        ResponsavelPermission,
    ]


class EmailPessoaViewSet(viewsets.ModelViewSet):
    queryset = EmailPessoa.objects.all()
    serializer_class = EmailPessoaSerializer
    permission_classes = [
        ResponsavelPermission,
    ]


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [
        AlunoPermission,
    ]


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    permission_classes = [
        ResponsavelPermission,
    ]


class BoletimViewSet(viewsets.ModelViewSet):
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer
    permission_classes = [
        BoletimPermission,
    ]


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [
        AvaliacaoPermission,
    ]


class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
    permission_classes = [
        FrequenciaPermission,
    ]


class DiaLetivoViewSet(viewsets.ModelViewSet):
    queryset = DiaLetivo.objects.all()
    serializer_class = DiaLetivoSerializer
    permission_classes = [
        DiaLetivoPermission,
    ]


class TransporteViewSet(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer
    permission_classes = [
        TransportePermission,
    ]


class TelefoneTransporteViewSet(viewsets.ModelViewSet):
    queryset = TelefoneTransporte.objects.all()
    serializer_class = TelefoneTransporteSerializer
    permission_classes = [
        TransportePermission,
    ]


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [
        FuncionarioPermission,
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            # Se o usuário é um superusuário, retorna todos os registros
            return Funcionario.objects.all()

        if user.groups.filter(name='Professores').exists():
            # Se o usuário é um Professor, retorna apenas seu próprio registro
            return Funcionario.objects.filter(usuario=user)

        if user.groups.filter(name='Coordenadores').exists():
            # Se o usuário é um Coordenador, retorna seu próprio registro e registros de Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name='Professores')

        if user.groups.filter(name='Diretores').exists():
            # Se o usuário é um Diretor, retorna seu próprio registro e registros de Coordenadores e Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name__in=['Coordenadores', 'Professores'])

        # Se nenhuma condição acima for satisfeita, retorna uma queryset vazia
        return Funcionario.objects.none()