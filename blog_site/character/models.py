from django.db import models

# Create your models here.
class CharacterModel(models.Model):
    characterName = models.CharField(max_length=20)
    characterImg = models.ImageField()
    characterDes = models.TextField()