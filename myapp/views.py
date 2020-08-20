from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return HttpResponse("<h1> Starting development server at http://127.0.0.1:8000/</h1>")

def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}</h1>".format(foods,languages))
    return render(request,'multiselect.html')

#uploading and display the uploaded image
"""
def img_upload(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        print(image)
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)

    return render(request,"img_upload.html",context={'file_url':file_url})
"""
def img_upload(request):
    return render(request,"img_upload.html")

def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        file_urls=[]
        #image=request.FILES.getlist('sam')
        image1=request.FILES.get('sam1')
        image2=request.FILES.get('sam2')
        print(image1,image2)
        for i in [image1,image2]:
            fs=FileSystemStorage()
            #file=fs.save(image.name,image)
            file=fs.save(i.name,i)
            file_url=fs.url(file)
            file_urls.append(file_url)

    return render(request,"img_display.html",context={'file_urls':file_urls})