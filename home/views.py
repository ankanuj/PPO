from django.shortcuts import render
from .models import ppo
from workers.models import Worker
def index(request):
	photo = ppo.objects.all()
	context = {
		'photo':photo,
	}
	return render(request,'home/index.html',context)

def about(request):
	img = ppo.objects.all()
	photo = Worker.objects.all()
	context = {
		'img':img,
		'photo':photo,
	}
	return render(request,'home/about.html',context)