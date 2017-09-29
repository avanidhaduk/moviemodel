from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from movieapp.forms import MyMovieForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_model(request):
	if request.method =="POST":
		form = MyMovieForm(request.POST)
		if form.is_valid():
			m1=form.save()
			m1.save()

			actor=request.POST.get('actor')
			actor_movie=request.POST.get('actor_movie')
			gener=request.POST.get('gener')

			context={'actor':actor,'actor_movie':actor_movie,'gener':gener}
			return render(request,"fetch.html",context)
	else:
		form=MyMovieForm()
		return render(request,"insert.html",{'form':form})