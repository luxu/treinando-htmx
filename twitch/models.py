from django.db import models

class Game(models.Model):
    name = models.CharField(
        "Nome",
        max_length=30
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['-id']


class Streamer(models.Model):
    name = models.CharField(
        "Nome",
        max_length=20
    )
    game = models.ForeignKey(
        Game,
        related_name="games",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Criador de conteúdo'
        verbose_name_plural = 'Criadores de conteúdo'
        ordering = ['-id']
