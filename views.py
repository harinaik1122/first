from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def surajana(request):
    return HttpResponse('<b>surajana is good girl</b>')
def hari(request):
    return HttpResponse('<marque>brothar of parameswar</marque>')