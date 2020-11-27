from .category import Category
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    game_image = models.ImageField(verbose_name='game_image', name='image1', width_field='300',height_field='300')
    categories = models.ManyToManyField(Category)
