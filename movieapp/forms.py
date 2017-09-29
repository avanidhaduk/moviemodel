from django.forms import ModelForm
from movieapp.models import Movie

class MyMovieForm(ModelForm):
	class Meta:
		model=Movie
		fields=['actor','actor_movie','gener']