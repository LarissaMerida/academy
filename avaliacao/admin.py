from django.contrib import admin
from .models import *

# Register your models here.
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'ativo',)
    list_filter = ('ativo',)
    search_fields = ['tipo']

    model = Avaliacao

admin.site.register(Avaliacao, AvaliacaoAdmin,)
