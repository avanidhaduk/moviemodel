from django.db import models

# Create your models here.
class Movie(models.Model):
	actor=models.CharField(max_length=30)
	actor_movie=models.CharField(max_length=50)
	gener=models.CharField(max_length=50)

	def __str__(self):
		return self.actor + '---'+ self.actor_movie + '---'+ self.gener