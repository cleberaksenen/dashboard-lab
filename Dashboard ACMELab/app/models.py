from django.db import models

#Chaves estrangeiras de RedcapSC2
class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Repeticao(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Variante(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Qualidade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Resultado(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#Classe da tabela do banco de dados de SARS-CoV-2
class SC2(models.Model):
    id = models.AutoField(primary_key=True) #ID
    record_id = models.CharField(max_length=200, default=0)
    codigo_interno = models.CharField(max_length=200) #String
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT, related_name='SC2_labs', default=0)
    estado = models.CharField(max_length=2, blank=True, null=True)
    mes_coleta = models.CharField(max_length=7, blank=True, null=True)

    lote = models.IntegerField() #Número inteiro
    melhor_repeticao = models.ForeignKey(Repeticao, on_delete=models.PROTECT, related_name='SC2_repet', default=0)
    cobertura = models.FloatField() #Número flutuante
    profundidade_media = models.FloatField()
    linhagem = models.CharField(max_length=50, blank=True, null=True)
    variante = models.ForeignKey(Variante, on_delete=models.PROTECT, related_name='SC2_var', default=0)
    qualidade = models.ForeignKey(Qualidade, on_delete=models.PROTECT, related_name='SC2_qua', default=0)
    resultado = models.ForeignKey(Resultado, on_delete=models.PROTECT, related_name='SC2_res', default=0)

    def __str__(self):
        return self.codigo_interno
    


