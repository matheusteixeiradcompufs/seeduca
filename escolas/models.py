from django.db import models
from django.utils import timezone


class Escola(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    num_salas = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='escola_images/', blank=True, null=True, default='')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.atualizado_em = timezone.now()
        if not self.pk:
            self.criado_em = timezone.now()
        super().save(*args, **kwargs)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero


class TelefoneEscola(Telefone):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True, related_name='escola_telefones')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'telefone'


class Email(models.Model):
    endereco = models.EmailField()

    def __str__(self):
        return self.endereco


class EmailEscola(Email):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True, related_name='escola_emails')

    def __str__(self):
        return self.endereco

    class Meta:
        verbose_name = 'e-mail'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)


class Sala(models.Model):
    numero = models.IntegerField()
    quantidade_alunos = models.IntegerField(null=True, blank=True)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True, related_name='escola_salas'),

    def __str__(self):
        return '{:03}'.format(self.numero)


class AgendaEscolar(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'agendas escolares'


class DiaAgenda(models.Model):
    data = models.DateField(unique=True)
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_dias')
    agenda = models.ForeignKey(AgendaEscolar, blank=True, null=True, on_delete=models.CASCADE, related_name='agenda_dias')


class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', blank=True, null=True, on_delete=models.CASCADE, related_name='dia_avisos')


class Tarefa(models.Model):
    descricao = models.TextField()
    tipo = models.BooleanField(default=False)
    cadastrada_em = models.DateTimeField(auto_now_add=True)
    entrega = models.DateTimeField(blank=True, null=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', blank=True, null=True, on_delete=models.CASCADE, related_name='dia_tarefas')


class ItemCardapioMerenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'ítem do cardápio'
        verbose_name_plural = 'ítens do cardápioy'


class CardapioMerenda(models.Model):
    item = models.ManyToManyField(ItemCardapioMerenda, blank=True, related_name='cardapios_itens')
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', blank=True, null=True, on_delete=models.CASCADE, related_name='dia_cardapios')

    class Meta:
        verbose_name = 'cardápio da merenda'
        verbose_name_plural = 'cardápios da merenda'


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    turno = models.CharField(max_length=10)
    sala = models.ForeignKey(Sala, null=True, blank=True, on_delete=models.CASCADE, related_name='sala_turmas')
    agenda = models.OneToOneField(AgendaEscolar, blank=True, null=True, on_delete=models.CASCADE, related_name='agenda_turma')
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_turmas')

    class Meta:
        unique_together = ['nome', 'ano', 'turno']

    def __str__(self):
        return self.nome