from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def CalPage(request):
    return render(request, 'calpage.html')

def Cal(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a) + int(value_b)
    return render(request, 'result.html', context={'result':result})