from django.shortcuts import render

# Create your views here.
def batman(request):
    return render(request,'Dc/batman.html')