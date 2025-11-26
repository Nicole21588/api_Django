from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    nivel = models.IntegerField()
    habilidade_especial = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    estudio_produtora = models.CharField(max_length=100)


class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class AtorDublador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    data_nascimento = models.DateField()

class Relacionamento(models.Model):
    id_personagem_origem = models.IntegerField()
    id_personagem_destino = models.IntegerField()
    tipo_relacionamento = models.CharField(max_length=50)