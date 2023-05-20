from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def survey(request):
    return render(request, 'survey.html')

def result(request, clas):
    return render(request, 'result.html', {'clas': clas})