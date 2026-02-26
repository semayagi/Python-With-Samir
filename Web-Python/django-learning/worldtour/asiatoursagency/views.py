from django.shortcuts import render
from django.http import HttpResponse

# Default: get
def index(request):
    return HttpResponse("Asia Tours Agency")
