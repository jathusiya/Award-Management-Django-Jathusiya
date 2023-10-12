from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from . models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from award_management import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes,force_text
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from .tokens import generate_token

def school(request):
    school = School.objects.all()
    return render(request,"awards/school.html",{"school": school})

def home(request):
    return render(request,"awards/home.html")

def subject(request):
    subject = Subject.objects.all()
    return render(request,"awards/subject.html",{"subject": subject})

def student(request):
    student = Student.objects.all()
    return render(request,"awards/student.html",{"student": student})

def classes(request):
    classes = Classes.objects.all()
    return render(request,"awards/classes.html",{"classes":classes})

def award(request):
    award = Award.objects.all()
    return render(request,"awards/award.html",{"award":award})

def answer(request):
    answer = Answer.objects.all()
    return render(request,"awards/answer.html",{"answer":answer})

def assessment(request):
    assessment = Assessment.objects.all()
    return render(request,"awards/assessment.html",{"assessment":assessment})

def summary(request):
    summary = Summary.objects.all()
    return render(request,"awards/summary.html",{"summary":summary})

@csrf_protect
def signup(request):  
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password =request.POST['password']
        password1 =request.POST['password1']
        
        if User.objects.filter(username=username):
            messages.error(request, "username already exist! Please try some other username")
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('/')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        if password != password1:
            messages.error(request, "Password did not match")
        
        if not username.isalnum():
            messages.error(request, "username must be Alpha-numeric")
            return redirect('/')
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        
        messages.success(request, "Your Account Successfully created.")
        
        #welcome Email
        
        subject = "Welcome To Reward"
        message = "Hello!" +myuser.first_name  + " !! \n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email,to_list, fail_silently = True)
        
        #Email Address confirmation Email
        
        current_site = get_current_site(request)
        email_subject = "confirm your email @ award - Loin!!"
        message2 = render_to_string('email_confirmation.html',{
            'name':myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        
        email.fail_silently = True
        email.send()
        return redirect('/signin')
        
    return render(request,"awards/auth/signup.html",{"signup":signup})

@csrf_protect
def signin(request):
     if request.user.is_authenticated:
        return redirect("/")
     else:
       if request.method == 'POST':
          name=request.POST.get('username').strip()
          pwd=request.POST.get('password').strip()
          user=authenticate(request,username=name,password=pwd)
          
          if user is not None:
             login(request,user)
             messages.success(request,"Login Successfully")
             return redirect("/")   
          else:
             messages.error(request,"Invalid User Name or Password")
             return redirect("signin")
         
       return render(request, "awards/auth/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('/')

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         myuser = None
        
#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         myuser.save()
#         login(request, myuser)
#         return redirect('/')
#     else:
#         return render(request, 'activation_failed.html')

def activate(request, uid64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and default_token_generator.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        return redirect('/')
    else:
        # Handle the case where activation fails (e.g., show an error page)
        return render(request, 'activation_failed.html')