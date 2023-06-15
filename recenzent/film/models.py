from django.db import models

# Create your models here.
class Film(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='film/images/')
    url=models.URLField(blank=True)
    year=models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' - ' + str(self.year) + ' r.' 
    
    class Meta:
        verbose_name_plural = 'Filmy'