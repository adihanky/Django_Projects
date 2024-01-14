from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app4/index.html")

def other(request):
    return render(request, "app4/other.html")

def relative(request):
    return render(request, "app4/relative.html")
