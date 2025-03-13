from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Cources
# # Create your views here.

def home(request):
    cour=Cources.objects.filter(active='t')
    context ={ 'cour': cour  }
    
    return render(request, 'course/index.html' , context )

# Delete course view
def dele(request, id):
     course = Cources.objects.get(id=id)
     course.active ='f'
     course.save()
     return redirect('/system')


def update(request, id):
    course = Cources.objects.get(id=id)

    if request.method == "POST":
        course.cource_name = request.POST.get('cource_name', course.cource_name)
        course.save()
        return redirect('/system') 

    return render(request, 'course/update_cource.html', {'course': course})  

def add(request):
    if request.method == "POST":
        cource_name = request.POST.get("cource_name")
        img = request.FILES.get("img")  
        # img_url = request.POST.get("img")
        # if 'http' not in img_url:
        #     img_url = 'media/' + img_url 
        if cource_name:
            Cources.objects.create(cource_name=cource_name, img=img , active='t')
            return redirect("/system") 

    return render(request, "course/add_course.html")