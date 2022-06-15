from django.db import models



class City(models.Model):
    locality = models.CharField(
        "Localidade",
        max_length=30
    )

    def __str__(self):
        return self.locality

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Radio(models.Model):
    name = models.CharField(
        "Nome",
        max_length=20
    )
    dial = models.CharField(
        "Canal",
        max_length=5
    )
    cities = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rádio"
        verbose_name_plural = "Rádios"
