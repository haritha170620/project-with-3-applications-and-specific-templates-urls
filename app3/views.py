from django.shortcuts import render

# Create your views here.
def three(request):
    return render(request,'three.html')