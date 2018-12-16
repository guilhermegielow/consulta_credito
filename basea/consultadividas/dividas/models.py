from django.db import models
from uuid import uuid4


class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cep = models.IntegerField()
    numero = models.IntegerField()
    bairro = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return "%s %s %s" % (self.logradouro, self.cidade, self.uf)


class Sacado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf = models.IntegerField(unique=True)
    nome = models.CharField(max_length=60)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf

    class Meta:
        ordering = ('cpf',)


class Cedente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf_cnpj = models.IntegerField(unique=True)
    nome = models.CharField(max_length=60)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf_cnpj

    class Meta:
        ordering = ('cpf_cnpj',)


class Divida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    valor = models.FloatField()
    vencimento = models.DateField()
    documento = models.CharField(max_length=20)
    cedente_id = models.ForeignKey(Cedente,  on_delete=models.CASCADE)
    sacado_id = models.ForeignKey(Sacado, on_delete=models.CASCADE)
    valor_multa = models.FloatField()
    valor_juros = models.FloatField()
    parcela = models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (self.documento, self.vencimento, self.valor)

    class Meta:
        ordering = ('sacado_id',)
