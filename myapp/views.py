from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Starting development server at http://127.0.0.1:8000/</h1>")

def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}</h1>".format(foods,languages))
    return render(request,'multiselect.html')