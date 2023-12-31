from rest_framework import serializers

from escolas.models import Escola, TelefoneEscola, EmailEscola, Disciplina, Sala, AgendaEscolar, DiaAgenda, Aviso, \
    Tarefa, ItemCardapioMerenda, CardapioMerenda, Turma


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [
            'id',
            'nome',
        ]


class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'diaAgenda',
        ]


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = [
            'id',
            'nome',
            'descricao',
            'tipo',
            'cadastrada_em',
            'entrega',
            'diaAgenda',
        ]


class DiaAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaAgenda
        fields = [
            'id',
            'data',
            'disciplina',
            'agenda',
            'objetos_avisos',
            'objetos_tarefas',
        ]
    objetos_avisos = AvisoSerializer(
        many=True,
        source='dia_avisos',
        read_only=True,
    )
    objetos_tarefas = TarefaSerializer(
        many=True,
        source='dia_tarefas',
        read_only=True,
    )


class AgendaEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaEscolar
        fields = [
            'id',
            'turma',
            'objetos_dias',
        ]
    objetos_dias = DiaAgendaSerializer(
        many=True,
        source='agenda_dias',
        read_only=True,
    )


class TelefoneEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneEscola
        fields = [
            'id',
            'numero',
            'escola',
        ]


class EmailEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailEscola
        fields = [
            'id',
            'endereco',
            'escola',
        ]


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'id',
            'nome',
            'ano',
            'turno',
            'sala',
            'disciplina',
            'objeto_agenda',
            'objetos_disciplinas',
        ]
    objeto_agenda = AgendaEscolarSerializer(
        many=False,
        source='turma_agenda',
        read_only=True,
    )
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplina',
        read_only=True,
    )


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            'id',
            'numero',
            'quantidade_alunos',
            'escola',
            'objetos_turmas',
        ]
    objetos_turmas = TurmaSerializer(
        many=True,
        source='sala_turmas',
        read_only=True,
    )


class ItemCardapioMerendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCardapioMerenda
        fields = [
            'id',
            'nome',
            'descricao',
        ]


class CardapioMerendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardapioMerenda
        fields = [
            'id',
            'data',
            'turno',
            'item',
            'escola',
            'objetos_itens',
        ]
    objetos_itens = ItemCardapioMerendaSerializer(
        many=True,
        source='item',
        read_only=True,
    )


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = [
            'id',
            'cnpj',
            'nome',
            'endereco',
            'num_salas',
            'descricao',
            'criado_em',
            'atualizado_em',
            'imagem',
            'objetos_telefones',
            'objetos_emails',
            'objetos_salas',
            'objetos_cardapios',
        ]
    objetos_telefones = TelefoneEscolaSerializer(
        many=True,
        source='escola_telefones',
        read_only=True,
    )
    objetos_emails = EmailEscolaSerializer(
        many=True,
        source='escola_emails',
        read_only=True,
    )
    objetos_salas = SalaSerializer(
        many=True,
        source='escola_salas',
        read_only=True,
    )
    objetos_cardapios = CardapioMerendaSerializer(
        many=True,
        source='escola_cardapios',
        read_only=True,
    )