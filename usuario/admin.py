from django.contrib import admin

# Register your models here.
from .models import Sorteio, Premio, Dezena

@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('numeroEdicao',  'anoEdicao', 'dataEdicao') # Exibe esses campos na lista do admin
    search_fields = ('numeroEdicao', 'anoEdicao') # Permite buscar por numero e ano da edição
    list_filter = ['anoEdicao'] # Filtro Lateral por ano

@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('sorteio', 'ordemPremio')
    list_filter = ['sorteio']

@admin.register(Dezena)
class DezenaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'premio')
    list_filter = ['premio']