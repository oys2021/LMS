from cgi import print_form
from email.mime import image
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
import time
from datetime import datetime
from .models import *
# from .forms import PostCourse
# Create your views here.
from django.core.checks import messages
from django.http import response
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
import json


from EDU.models import Courses
from EDU.models import Profile
from EDU.forms  import ProfileForm
 



def home(request):
    return render(request,"EDU/index.html")


def courses(request):
    courses=Everything.objects.all()
    context={"courses":courses}
    return render(request,"EDU/courses.html",context)



def contact(request):
    return render(request,"EDU/contact.html",{})

def teacher_view(request):
    return render(request,"EDU/teacher.html",{})


def about(request):
    return render(request,"EDU/about.html",{})


def login(request):
    if request.method=="POST":
        username=request.POST["user"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/courses")
        else:
            print("BYE")

    else:
        return render(request,"EDU/log.html",{})

def test(request):
    return render(request,"EDU/test.html",{})

   
       

    

def signup(request):
    if request.method=="POST":
        first_name=request.POST["first"]
        last_name=request.POST["last"]
        username=request.POST["user"]
        password1=request.POST["p1"]
        password2=request.POST["p2"]
        email=request.POST["email"]

        if password1==password2:
             user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
             user.save()
             return redirect("/courses")
        else:
            print("Error")

    else:
        return render(request,"EDU/sindex.html",{})

        
def logout(request):
	auth.logout(request)
	return redirect("/")

#recover password
def recover_password(request):
    if request.method=="POST":
        username=request.POST["user"]
        new_password=request.POST["password1"]
        confirm_password=request.POST["password2"]

        if new_password==confirm_password:
            u=User.objects.get(username=username)
            u.set_password(new_password)
            u.save()
            return redirect("/courses")
        
    return render(request,"EDU/recover.html",{})


def enroll_update(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action=data["action"]
    courseitem = Everything.objects.get(id=productId)
    user=request.user.student
    course, created = Enroll.objects.get_or_create(everything=courseitem,student=user)

    if action == "add":
        course.save()
        return redirect("contact")
    else:
        return JsonResponse("You Have Enrolled", safe = False)

    
       
def create(request):
    if request.method=="POST":
        name=request.POST["name"]
        code=request.POST["code"]
        lecturer=request.POST["lecturer"]

        course=Everything.objects.create(name=name,classcode=code,lecturer=lecturer)
        course.save()
        return redirect("courses")
    else:
        return render(request,"EDU/createcourse.html",{})

def profile(request,username):
    user=User.objects.get(username=username)
    prof=request.user.profile
    form=ProfileForm(instance=prof)

    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=prof)
        if form.is_valid():
            form.save()

    context={"users":prof,"form":form}
    return render(request,"EDU/profile.html",context)

def course_detail(request,id):
    course = Student.objects.get(id=id).get_courses()
    return render(request, 'EDU/enrolled.html', {'course': course})      


def classes(request):
    student = request.user.student
    classes = student.get_classes()
    context = {'students': student, 'classes': classes,}
    return render(request, 'EDU/classes.html', context)


def lessons(request,id):
    lessons = Class.objects.get(id=id).get_lessons()
    context = {'lessons':lessons}
    return render(request,'EDU/lessons.html',context) 


def about_course(request):
    return render(request,'EDU/aboutcourse.html',{})

def coursepage(request,pk):
    course=Everything.objects.get(pk=pk)
    context={"course":course}
    return render(request,"EDU/coursepage.html",context)

    
       
     
   

        # watch dennis ivy youtube video and get inspired for logics.Then read on many to many,one to one etc.
   
   

    
    

# def enrolled_courses(request,user):
#     enroll=Enrolled_Courses.objects.get(user=user)
#    


    

    
# Next time we display the enrolled courses and go straight to the courses after and the button changes to GO TO COURSES or get strarted.
# We want to check if the button is clicked move to another page or do something added to the javascript functionality.

# def enrolled_courses(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         courses, created =Everything .objects.get_or_create(customer = customer, completed = False)
#         # cartitems = cart.cartitems_set.all()
#     else:
#         # cartitems = []
#         cart = {"get_cart_total": 0, "get_itemtotal": 0}


#     return render(request, 'YS/Enrolled_Courses.html', {'cart':cart})
#     # 'cartitems' : cartitems,


#we are set to  controlled the viewed enroll courses page.






    




        
        

        # you always have to loop through your queryset before rendering them here.
        


        
  


   
   





   
  
   
        



       
    
    
             
    








  

    
   
   



        

    









