from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'codedare_app/index.html', context)

def posts(request):
    context = {}
    return render(request, 'codedare_app/posts.html', context)