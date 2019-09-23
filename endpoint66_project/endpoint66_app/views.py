from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# def index(request):
#     return HttpResponse('Welcome Test')

def goge(request):
    return HttpResponse('Here you go! Graham crackers!')

def happyJoy(request):
    return HttpResponse("'Cuase I'm All That!")




def words_test(request, words):
    return HttpResponse(words)