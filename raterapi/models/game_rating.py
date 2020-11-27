from raterapi.models.game import Game
from django.db import models
from .game import Game
from .player import Player

class Game_rating(models.Model):

   game = models.ManyToManyField(Game)
   rating = models.IntegerField()
   player = models.ManyToManyField(Player)
