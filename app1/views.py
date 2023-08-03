from django.shortcuts import render

# Create your views here.
def specificstatic(request):
    return render(request,'specificstatic.html')

def specificstatic1(request):
    return render(request,'specificstatic1.html')