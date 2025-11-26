from rest_framework import serializers
from .models import Personagem, Obra, Habilidade, AtorDublador, Relacionamento

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = '__all__'

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = '__all__'

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtorDublador
        fields = '__all__'

class RelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionamento
        fields = '__all__'