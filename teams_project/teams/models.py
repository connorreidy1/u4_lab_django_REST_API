from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number_of_teams = models.PositiveIntegerField()
    year_founded = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    number_of_wins = models.IntegerField()
    number_of_draws = models.IntegerField(default=0)
    number_of_loses = models.IntegerField()
    team_logo = models.TextField()

    def __str__(self):
        return self.name
    

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField(choices=[(i, i) for i in range(1, 100)])
    injured = models.BooleanField(default=False)
    image_url =  models.TextField(default='')
    
    def __str__(self):
        return self.name
    