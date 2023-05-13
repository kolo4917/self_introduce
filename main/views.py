# Create your views here.
def index(request):
    return render(request, 'main/index.html')

from django.shortcuts import render

def page1_view(request):
    return render(request, 'page1.html')
def page2_view(request):
    return render(request, 'page2.html')
def page4_view(request):
    return render(request, 'page4.html')
def page5_view(request):
    return render(request, 'page5.html')

# Create your views here.
