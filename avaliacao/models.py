from django.db import models


# Create your models here.
class Avaliacao(models.Model):
    tipo = models.CharField(max_length=255)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
        
    class Meta:
        db_table = "avaliacao"
        verbose_name_plural = "Avaliações"