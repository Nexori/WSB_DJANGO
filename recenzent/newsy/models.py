from django.db import models

# Create your models here.
class Newsy(models.Model):
    naglowek=models.CharField(max_length=200)
    tresc=models.TextField()
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naglowek

    class Meta:
        verbose_name_plural = 'Newsy'
        ordering=['-data']

    