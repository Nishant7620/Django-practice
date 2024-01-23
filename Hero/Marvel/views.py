from django.shortcuts import render

# Create your views here.

def spiderman(request):
    context = {'name': 'Peter Parkar'}    
    return render(request,'Marvel/spiderman.html',context)