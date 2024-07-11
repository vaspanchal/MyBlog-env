from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This Is ME..\n I dont know Coding.\n i dont have anything to show here right now..\n soon you'll see!")