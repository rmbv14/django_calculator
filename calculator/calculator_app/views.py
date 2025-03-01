from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    if request.method == 'POST':
        result = request.POST.get('result', '')

        return render(request, 'base.html', {'result': result})

    return render(request, 'base.html')

# Create your views here.
