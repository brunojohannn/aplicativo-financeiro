from django.db import models

# Create your models here

class Transacao(models.Model):
  TIPO_CHOICES = [
    ('receita','Receita'),
    ('despesa','Despesa'),
  ]

  CATEGORIA_CHOICES = [
    ('credito','Credito'),
    ('debito', 'Debito'),
    ('pix', 'Pix'),
    ('boleto','Boleto'),
    ('dinheiro','Dinheiro'),
  ]

  descricao = models.CharField(max_length=255)
  valor = models.DecimalField(max_digits=10, decimal_places=2)
  tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
  categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
  data = models.DateTimeField(auto_now_add=True)

  def __str__ (self):
    return f"{self.descricao} - {self.tipo} - R$ {self.valor}"