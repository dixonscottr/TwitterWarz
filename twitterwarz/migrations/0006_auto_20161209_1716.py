# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 17:16
from __future__ import unicode_literals

from django.db import models, migrations
from twitterwarz.models import User, Tweet
from IPython import embed
import random

def load_battles(twitterwarz, schema_editor):
  Battle = twitterwarz.get_model('twitterwarz', 'Battle')
  users = User.objects.all()
  for user in users:
    for x in range(0, 2):
      attacking_user = user
      defending_user = random.choice(users)
      while defending_user == user:
        defending_user = random.choice(users)
      winning_user = attacking_user
      losing_user = defending_user
      b = Battle(attacker_id=attacking_user.id, defender_id=defending_user.id, winner_id=winning_user.id, loser_id=losing_user.id)
      b.save()

class Migration(migrations.Migration):

    dependencies = [
        ('twitterwarz', '0005_auto_20161209_1705'),
    ]

    operations = [
      migrations.RunPython(load_battles)
    ]
