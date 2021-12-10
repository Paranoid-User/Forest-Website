from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def trees(request):
    return render(request,'trees.html')

def woods_vs_forest(request):
    return render(request,'woods vs forest.html')

