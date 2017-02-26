# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint

def index(request):
    # random_numner = randint(1,10)
    # return HttpResponse("Hello, world. You're at the index. {}".format(random_numner))
    name = "taehwan"
    return render(request, "index.html", {"name" : name})


# Create your views here.
