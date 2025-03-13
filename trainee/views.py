from django.shortcuts import render , redirect
from .models import Trainee
from course.models import Cources
# Create your views here.

def home(request):
    cour=Cources.objects.filter(active='t')
    context={'cour' : cour}
    return render(request,'trainee/index.html' , context)

def sign(request):
    cour = Cources.objects.filter(active='t')
    context = {'cour' : cour }
    if request.method == 'POST' :
        user =  request.POST.get('user')
        email = request.POST.get('email')
        password=request.POST.get('password')
        course_id = request.POST.get('course_id')

        selected = Cources.objects.get( id = course_id)

        Trainee.objects.create( username_field = user , email = email , password = password ,cid=selected)        
        return redirect ('/login')
    
    return render(request , 'trainee/signup.html' ,context) 

def log(request):
    if request.method == 'POST':
        usern = request.POST.get("user")
        passw = request.POST.get("password")

        train = Trainee.objects.filter(username_field=usern, password=passw).first()
        if train:
            request.session['user_id'] = train.id 
            return redirect('/profile')  
    return render(request, 'trainee/login.html')

def pro(request):
    user_id = request.session.get('user_id')  

    train = Trainee.objects.get(id=user_id)  
    cour = Cources.objects.filter(id=train.cid.id).first() 

    context = {'train': train, 'cour': cour}
    return render(request, 'trainee/profile.html', context)