from django.shortcuts import render

def indexx(request):
    return render(request, 'index.html')
