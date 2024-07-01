from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'Hello World', 'number': 5000}
    return render(request, 'Basic_App/index.html')

def other(request):
    return render(request, 'Basic_App/other.html')

def relative(request):
    return render(request, 'Basic_App/relative_url.html')