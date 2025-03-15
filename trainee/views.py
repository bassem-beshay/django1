from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course.models import Cources
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
        
        
        errors = {}
        if len(user) < 3:
            errors["user"] = "you should enter name more  3 character"
        elif not re.match(r"^[a-zA-Z0-9_]+$", user):
            errors["user"] = "you should enter name contain name plus num"

        if "@" not in email or "." not in email:
            errors["email"] = "you shoul enter email valid"

        if len(password) < 5:
            errors["password"] = "password should be more than 5 character"
        elif not re.fullmatch(r"\d+", password):
            errors = {"password": "password should contain number"}


        selected = get_object_or_404(Cources, id=course_id)    

        if errors:
            return render(request, "trainee/signup.html", {"errors": errors, "cour": cour})
        
        Trainee.objects.create( username_field = user , email = email , password = password ,cid=selected)  
      
        # trainee.save()
        # if  eccrypt password
        # trainee = Trainee(username_field=user, email=email, cid=selected)
        # trainee.set_password(password)  
        # trainee.save()
        
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
        else:
            return render(request, 'trainee/login.html', {'error': 'invalid username'})
    return render(request, 'trainee/login.html')

def pro(request):
    try:
        user_id = request.session.get('user_id')
        train = Trainee.objects.get(id=user_id)  
        cour = Cources.objects.filter(id=train.cid.id).first() 

        context = {'train': train, 'cour': cour}

    except:
        return redirect('/login')      

    
    return render(request, 'trainee/profile.html', context)


def logout(request):
    request.session.flush()
    return redirect('/login')
