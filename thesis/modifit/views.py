from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'modifit/index.html', {})

def wardrobe(request, wardrobe_id):
	response = "Wardrobe ID: " + str(wardrobe_id)
	user = 1;
	return render(request, 'modifit/wardrobe.html', { 'response' : response, 'user' : user })