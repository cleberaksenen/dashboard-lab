from django.contrib import admin
from app.models import Laboratorio
from app.models import Repeticao
from app.models import Variante
from app.models import Qualidade
from app.models import Resultado
from app.models import SC2

#Configurando...
class Laboratorio_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class Repeticao_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class Variante_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class Qualidade_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class Resultado_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class SC2_admin(admin.ModelAdmin):
    list_display = ('id', 'codigo_interno', 'laboratorio', 'estado', 'mes_coleta', 'lote',
                    'melhor_repeticao', 'cobertura', 'profundidade_media', 'linhagem', 'variante',
                    'qualidade', 'resultado')
    search_fields = ('id', 'codigo_interno', 'laboratorio', 'estado', 'mes_coleta', 'lote',
                    'melhor_repeticao', 'cobertura', 'profundidade_media', 'linhagem', 'variante',
                    'qualidade', 'resultado')

#Registrando...
admin.site.register(Laboratorio, Laboratorio_admin)
admin.site.register(Repeticao, Repeticao_admin)
admin.site.register(Variante, Variante_admin)
admin.site.register(Qualidade, Qualidade_admin)
admin.site.register(Resultado, Resultado_admin)

admin.site.register(SC2, SC2_admin)
