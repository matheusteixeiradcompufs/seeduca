from django.db import models
from django.utils import timezone


class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = []
        kwargs['choices'] = [(i, i) for i in range(1900, 2101)]
        super().__init__(*args, **kwargs)


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
        return str(self.nome)

    def save(self, *args, **kwargs):
        self.atualizado_em = timezone.now()
        if not self.pk:
            self.criado_em = timezone.now()
        super().save(*args, **kwargs)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)

    def __str__(self):
        return str(self.numero)


class TelefoneEscola(Telefone):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_telefones')

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name = 'telefone'


class Email(models.Model):
    endereco = models.EmailField()

    def __str__(self):
        return str(self.endereco)


class EmailEscola(Email):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_emails')

    def __str__(self):
        return str(self.endereco)

    class Meta:
        verbose_name = 'e-mail'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.nome)


class Sala(models.Model):
    numero = models.IntegerField(unique=True)
    quantidade_alunos = models.IntegerField(null=True, blank=True)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_salas')

    def __str__(self):
        return '{:03}'.format(self.numero)


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = YearField()
    turno = models.CharField(max_length=10)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sala_turmas')
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_turmas')

    def __str__(self):
        return str(self.nome)

    class Meta:
        unique_together = ['nome', 'ano', 'turno']


class AgendaEscolar(models.Model):
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='turma_agenda')

    def __str__(self):
        return 'Agenda do ' + str(self.turma)

    class Meta:
        verbose_name = 'agenda escolar'
        verbose_name_plural = 'agendas escolares'


class DiaAgenda(models.Model):
    data = models.DateField()
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_dias')
    agenda = models.ForeignKey(AgendaEscolar, on_delete=models.CASCADE, related_name='agenda_dias')

    def __str__(self):
        return str(self.data)

    class Meta:
        verbose_name = 'dia da agenda'
        verbose_name_plural = 'dias da agenda'
        unique_together = ['data', 'agenda']


class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', on_delete=models.CASCADE, related_name='dia_avisos')

    def __str__(self):
        return str(self.titulo)


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.BooleanField(default=False)
    cadastrada_em = models.DateTimeField(auto_now_add=True)
    entrega = models.DateTimeField(blank=True, null=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', on_delete=models.CASCADE, related_name='dia_tarefas')

    def __str__(self):
        return str(self.nome)


class ItemCardapioMerenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'ítem do cardápio'
        verbose_name_plural = 'ítens do cardápio'


class CardapioMerenda(models.Model):
    data = models.DateField()
    turno = models.CharField(max_length=50, blank=True, null=True)
    item = models.ManyToManyField(ItemCardapioMerenda, blank=True, related_name='cardapios_itens')
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_cardapios')

    def __str__(self):
        return 'Cardápio ' + str(self.data) + ' turno ' + str(self.turno)

    class Meta:
        verbose_name = 'cardápio da merenda'
        verbose_name_plural = 'cardápios da merenda'
        unique_together = ['data', 'turno']