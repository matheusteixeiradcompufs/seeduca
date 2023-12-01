from django.contrib.auth.models import User
from django.db import models

from escolas.models import Escola


class Pessoa(models.Model):
    matricula = models.CharField(max_length=10, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='pessoa_telefones')

    def __str__(self):
        return self.numero


class Email(models.Model):
    endereco = models.EmailField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='pessoa_emails')

    def __str__(self):
        return self.endereco


class Aluno(Pessoa):
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT, related_name='escola_alunos')

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
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT, related_name='escola_funcionarios')

    def __str__(self):
        return str(self.usuario)

