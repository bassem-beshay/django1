from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Cources
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
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



@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET': 
        courses = Cources.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Cources.objects.get(pk=pk)
    except Cources.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)