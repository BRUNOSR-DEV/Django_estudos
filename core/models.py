from django.db import models

"""
modelo de dados, atráves do models que você vai conseguir percistir com o banco de dados

"""
class Produto(models.Model):

    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self) -> str:
        return self.nome


class Cliente(models.Model):
    
    nome = models.CharField('Nome', max_length=100)
    sobrenome =  models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self) -> str:
        return f'{self.nome}  {self.sobrenome}'