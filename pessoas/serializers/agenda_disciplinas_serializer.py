from rest_framework import serializers

from escolas.models import AgendaEscolar


class IntListField(serializers.ListField):
    """
    Um campo serializador personalizado para listas de inteiros.
    """
    child = serializers.IntegerField()

    def to_internal_value(self, data):
        """
        Converte os dados recebidos em uma lista de inteiros.
        """
        if not all(isinstance(item, int) for item in data):
            self.fail('invalid')
        return super().to_internal_value(data)


class AgendaDisciplinasSerializer(serializers.Serializer):
    """
    Serializador para a atribuição de disciplinas a dias específicos em uma agenda escolar.
    """
    agenda_id = serializers.IntegerField()
    seg = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    ter = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    qua = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    qui = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    sex = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})

    @staticmethod
    def validate_agenda_id(value):
        """
        Valida se o ID da agenda existe no banco de dados.
        """
        try:
            AgendaEscolar.objects.get(id=value)
        except AgendaEscolar.DoesNotExist:
            raise serializers.ValidationError("Agenda não encontrada.")
        return value

    def create(self, validated_data):
        """
        Criação de associações de disciplinas a dias específicos na agenda escolar.
        """
        agenda_id = validated_data.pop('agenda_id')
        seg = validated_data.pop('seg')
        ter = validated_data.pop('ter')
        qua = validated_data.pop('qua')
        qui = validated_data.pop('qui')
        sex = validated_data.pop('sex')

        disciplinas_por_dia = [seg, ter, qua, qui, sex]

        # Obtém a agenda escolar correspondente ao ID fornecido
        agenda = AgendaEscolar.objects.filter(pk=agenda_id).first()
        dias_agenda = agenda.agenda_dias.filter(util=True)

        # Associa as disciplinas aos dias correspondentes
        for dia in dias_agenda:
            dia.disciplinas.set(disciplinas_por_dia[dia.data.weekday()])

        return agenda_id

    def update(self, instance, validated_data):
        """
        Atualiza as associações de disciplinas a dias específicos na agenda escolar.
        """
        super(AgendaDisciplinasSerializer, self).update(instance, validated_data)

