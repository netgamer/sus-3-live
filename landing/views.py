from django.shortcuts import render

def landing(requset):
    return render(requset, "landing/index.html")
