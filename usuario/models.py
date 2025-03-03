from django.db import models

# Create your models here.
class Sorteio(models.Model):
    numeroEdicao = models.IntegerField() # Número da Edição
    anoEdicao = models.IntegerField() # Ano da Edição
    dataEdicao = models.DateField() #Data do Sorteio

    def __str__(self):
        return f"Edição {self.numeroEdicao}/{self.anoEdicao}"
    

class Premio(models.Model):
    sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE, related_name="premios")
    ordemPremio = models.IntegerField() # Ordem da premiação

    def __str__(self):
        return f"{self.ordemPremio}º Prêmio - {self.sorteio}"
    
class Dezena(models.Model):
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE, related_name="dezenas")
    numero = models.IntegerField() #Numeros sorteados

    def __str__(self):
        return f"{self.numero} - {self.premio}"