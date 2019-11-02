from django.shortcuts import render

def blog(request):
    return render(request, 'GASnake/snk.html')
