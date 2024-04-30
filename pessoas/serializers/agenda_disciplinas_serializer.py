from rest_framework import serializers

from escolas.models import AgendaEscolar, DiaAgenda, Disciplina


class IntListField(serializers.ListField):
    child = serializers.IntegerField()

    def to_internal_value(self, data):
        if not all(isinstance(item, int) for item in data):
            self.fail('invalid')
        return super().to_internal_value(data)


class AgendaDisciplinasSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    seg = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    ter = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    qua = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    qui = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})
    sex = IntListField(child=serializers.IntegerField(), error_messages={'required': 'Este campo é obrigatório', 'invalid': 'Este campo precisa ser um vetor de inteiros'})

    def validate_agenda_id(self, value):
        try:
            AgendaEscolar.objects.get(id=value)
        except AgendaEscolar.DoesNotExist:
            raise serializers.ValidationError("Agenda não encontrada.")
        return value

    def create(self, validated_data):
        agenda_id = validated_data.pop('agenda_id')
        seg = validated_data.pop('seg')
        ter = validated_data.pop('ter')
        qua = validated_data.pop('qua')
        qui = validated_data.pop('qui')
        sex = validated_data.pop('sex')

        disciplinas_por_dia = [seg, ter, qua, qui, sex]

        agenda = AgendaEscolar.objects.filter(pk=agenda_id).first()
        dias_agenda = agenda.agenda_dias.filter(util=True)
        for dia in dias_agenda:
            dia.disciplinas.set(disciplinas_por_dia[dia.data.weekday()])

        return agenda_id
