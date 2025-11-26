from rest_framework import viewsets
from .models import Personagem, Obra, Habilidade, AtorDublador, Relacionamento
from .serializers import PersonagemSerializer, ObraSerializer, HabilidadeSerializer, AtorSerializer, RelacionamentoSerializer

class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer

class AtorViewSet(viewsets.ModelViewSet):
    queryset = AtorDublador.objects.all()
    serializer_class = AtorSerializer

class RelacionamentoViewSet(viewsets.ModelViewSet):
    queryset = Relacionamento.objects.all()
    serializer_class = RelacionamentoSerializer
    
 