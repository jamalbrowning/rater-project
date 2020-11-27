from raterapi.models.game import Game
from django.db import models
from .game import Game
from .player import Player

class Game_review(models.Model):

   game = models.ManyToManyField(Game)
   review = models.CharField(max_length=150)
   player = models.ManyToManyField(Player)
