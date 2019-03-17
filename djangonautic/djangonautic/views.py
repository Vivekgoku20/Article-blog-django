#Contains set of all callback functions to execute

from django.http import HttpResponse
from django.shortcuts import render


def homePage(req):
	#return HttpResponse('home page')
	return render(req, 'homepage.html')

def about(req):
	#return HttpResponse('about')
	return render(req, 'about.html')