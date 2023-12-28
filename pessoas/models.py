from django.contrib.auth.models import User
from django.db import models

from escolas.models import Escola, Disciplina, Turma, Telefone, Email, YearField


class Pessoa(models.Model):
    matricula = models.CharField(
        max_length=10,
        unique=True
    )
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True
    )
    endereco = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='usuario_pessoa'
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.PROTECT,
        related_name='escola_pessoas'
    )

    def __str__(self):
        return str(self.usuario)


class TelefonePessoa(Telefone):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pessoa_telefones'
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'telefone'


class EmailPessoa(Email):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pessoa_emails'
    )

    def __str__(self):
        return self.endereco

    class Meta:
        verbose_name = 'e-mail'


class Aluno(Pessoa):
    turma = models.ManyToManyField(
        Turma,
        blank=True,
        related_name='turmas_alunos'
    )

    def __str__(self):
        return str(self.usuario)


class EhPCD(models.Model):
    eh_pcd = models.BooleanField(
        default=False
    )
    descricao = models.TextField()
    aluno = models.OneToOneField(
        Aluno,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='aluno_pcd'
    )

    def __str__(self):
        return str(self.eh_pcd)

    class Meta:
        verbose_name = 'É PCD'


class Responsavel(models.Model):
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    nome = models.CharField(max_length=255)
    observacao = models.TextField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='aluno_responsaveis'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'responsável'
        verbose_name_plural = 'responsáveis'


class Funcionario(Pessoa):
    formacao = models.TextField(
        null=True,
        blank=True
    )
    turma = models.ManyToManyField(
        Turma,
        blank=True,
        related_name='turmas_funcionarios'
    )

    def __str__(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'funcionário'


class Boletim(models.Model):
    ano = YearField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins'
    )

    def __str__(self):
        return 'Boletim de ' + str(self.ano)

    class Meta:
        verbose_name_plural = 'boletins'


class Avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.FloatField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_avaliacoes'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_avaliacoes'
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_avaliacoes'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_avaliacoes'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'


class Frequencia(models.Model):
    nome = models.CharField(max_length=100)
    ano = YearField()
    percentual = models.FloatField(
        blank=True,
        null=True
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_frequencias'
    )

    def __str__(self):
        return 'Frequência em ' + str(self.ano)

    class Meta:
        verbose_name = 'frequência'


class DiaLetivo(models.Model):
    data = models.DateField()
    presenca = models.BooleanField(default=True)
    frequencia = models.ForeignKey(
        Frequencia,
        on_delete=models.CASCADE,
        related_name='frequencia_diasletivos'
    )

    def __str__(self):
        return self.data

    class Meta:
        verbose_name = 'dia letivo'
        verbose_name_plural = 'dias letivos'


class Transporte(models.Model):
    placa = models.CharField(max_length=7)
    ano = YearField()
    tipo = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='tipo do veículo',
    )
    nomeMotorista = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do motorista',
    )
    nomeAuxiliar = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do auxiliar',
    )
    itinerario = models.TextField(
        blank=True,
        null=True
    )
    aluno = models.ManyToManyField(
        Aluno,
        blank=True,
        related_name='alunos_transportes'
    )

    def __str__(self):
        return self.placa

    class Meta:
        unique_together = ['placa', 'ano']


class TelefoneTransporte(Telefone):
    transporte = models.ForeignKey(
        Transporte,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='transporte_telefones'
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'telefone'