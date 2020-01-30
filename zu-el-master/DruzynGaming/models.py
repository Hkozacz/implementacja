from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, help_text='Tytuł')
    message = models.TextField(help_text="Treść")

    def __str__(self):
        return self.title

class Player(models.Model):
    imie=models.CharField(max_length=30,help_text='Imie')
    nick=models.CharField(max_length=30,help_text='Nick')
    nazwisko=models.CharField(max_length=30,help_text='Nazwisko')
    sekcja=models.CharField(max_length=30,help_text='Sekcja')
    rola=models.CharField(max_length=30,help_text='Rola')

    def __str__(self):
        return (self.imie, self.nick, self.nazwisko)