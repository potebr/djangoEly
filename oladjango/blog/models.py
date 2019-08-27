from django.db import models

# Create your models here.
class Postman(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    resumo = models.CharField(max_length=100)
    def __str__(self):
        return self.autor

class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
        nome = models.CharField(max_length=100)
        cnpj = models.CharField(max_length=20)
        endereco = models.CharField(max_length=100)
        cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
        def __str__(self):
            return self.nome
class Cidade(models.Model):
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)
    def __str__(self):
        return self.cidade
    
