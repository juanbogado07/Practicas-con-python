from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index_1 (request):
    plantilla= loader.get_template('index.html')
