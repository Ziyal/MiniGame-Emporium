from django.shortcuts import render, redirect

def index(request):
    if "data" in request.session:
        request.session.clear()

    if "attempts" in request.session:
        request.session.clear()

    return render(request, 'home/index.html')
