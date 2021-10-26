from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse('hello from django app!')

def item(request):
	return HttpResponse(['working hard', 1998, True])