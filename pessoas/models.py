from django.contrib.auth.models import User
from django.db import models

from escolas.models import Escola, Disciplina, Turma, Telefone, Email


class Pessoa(models.Model):
    matricula = models.CharField(max_length=10, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_pessoa')
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT, related_name='escola_pessoas')

    def __str__(self):
        return str(self.usuario)


class TelefonePessoa(Telefone):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='pessoa_telefones')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'telefone'


class EmailPessoa(Email):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='pessoa_emails')

    def __str__(self):
        return self.endereco

    class Meta:
        verbose_name = 'e-mail'


class Transporte(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    nomeMotorista = models.CharField(max_length=100, blank=True, null=True)
    nomeAuxiliar = models.CharField(max_length=100, blank=True, null=True)
    itinerario = models.TextField(blank=True, null=True)


class TelefoneTransporte(Telefone):
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=True, blank=True, related_name='transporte_telefones')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'telefone'


class Aluno(Pessoa):
    transporte = models.ForeignKey(Transporte, blank=True, null=True, on_delete=models.PROTECT, related_name='transporte_alunos')
    turma = models.ManyToManyField(Turma, blank=True, related_name='turmas_alunos')

    def __str__(self):
        return str(self.usuario)


class EhPCD(models.Model):
    eh_pcd = models.BooleanField(default=False)
    descricao = models.TextField()
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, null=True, blank=True, related_name='aluno_pcd')

    def __str__(self):
        return str(self.eh_pcd)


class Responsavel(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    observacao = models.TextField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True, related_name='aluno_responsaveis')

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    formacao = models.TextField(null=True, blank=True)
    turma = models.ManyToManyField(Turma, blank=True, related_name='turmas_funcionarios')

    def __str__(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'funcionário'


class Boletim(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.DateField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='aluno_boletins')

    class Meta:
        verbose_name_plural = 'boletins'


class Avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.FloatField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='aluno_avaliacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplina_avaliacoes')
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE, related_name='boletim_avaliacoes')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='turma_avaliacoes')


class Frequencia(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.DateField()
    percentual = models.FloatField(blank=True, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='aluno_frequencias')

    class Meta:
        verbose_name = 'frequência'


class DiaLetivo(models.Model):
    data = models.DateField()
    presenca = models.BooleanField(default=True)
    frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE, related_name='frequencia_diasletivos')

    class Meta:
        verbose_name = 'dia letivo'
        verbose_name_plural = 'dias letivos'