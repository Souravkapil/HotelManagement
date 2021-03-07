from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
from django.core.mail import send_mail
from .models import Contact_table
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.

#def index(request):
#	return HttpResponse("<h1>hello django</h1>")

def signup(request):
	return render(request,'signup.html',{})

def login(request):
	return render(request,'login.html',{})

def index(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})

def room(request):
	return render(request,'room.html',{})

def gallery(request):
	return render(request,'gallery.html',{})

def reservation(request):
	return render(request,'reservation.html',{})

def contact(request):
	return render(request,'contact.html',{})

def contactValue(request):
	name = request.POST.get('name','default')
	mobile = request.POST.get('mob','default')
	email = request.POST.get('email','default')
	subject1 = request.POST.get('sub','default')
	msg = request.POST.get('msg','default')
	print(name,mobile,email,subject1,msg)
	con  = Contact_table.objects.create(Name=name,Mobile=mobile,Email=email,Subject=subject1,Message=msg)
	con.save()
	return HttpResponse("""<h1>Thanks for contact us.</h1> <a href='index'> Click here for Home Page</a>""")

def reservationvalue(request):
	name = request.POST.get('name','default')
	mobile = request.POST.get('mob','default')
	email = request.POST.get('email','default')
	checkin = request.POST.get('check1','default')
	checkout = request.POST.get('check2','default')
	adults = request.POST.get('adults','default')
	children = request.POST.get('children','default')
	select = request.POST.get('selectroom','default')
	number = request.POST.get('numbersofroom','default')
	print(name,mobile,email,checkin,checkout,adults,children,select,number)

	subject = 'Booking'
	message = "Name : "+name+"\n"+"Mobile : "+mobile+"\n"+"Email : "+email+"\n"+"Checkin : "+checkin+"\n"+"Checkout : \
	"+checkout+"\n"+"Adults : "+adults+"\n"+"Children : "+children+"\n"+"Room : "+select+"\n"+"Numbers of room : "+number
	email_from = settings.EMAIL_HOST_USER
	to  = "souravkapil2000@gmail.com"
	send_mail( subject, message, email_from, [to]) 


	return HttpResponse("""<h1>Rooms Available.</h1> <h2><strong>Welcome to SKYLINE Hotel.</strong></h2> 
		<p><em><strong> We are pleased to here you. Your 2 deluxe room are available. </strong></em></p> 
		<a href='index'> Click here for Home Page</a> <br><br> <a href='/about'> Click here for About</a> <br><br> 
		<a href='/room'> Click here for Rooms</a> <br><br> <a href='/gallery'> Click here for Gallery</a> <br><br> 
		<a href='/contact'> Clickrhere for Contact</a> <br><br> <strong>Thanks for Contact us.</strong>""")

def signup_data(request):
	username =request.POST.get('username')
	email =request.POST.get('email')
	password =request.POST.get('password')
	username_exist=User.objects.filter(username=username)
	if username_exist:
		return HttpResponse('Username Already Exist,Please Either login with same user Id or create new user')
	else:
		user=User.objects.create(username=username,email=email,password=password)
		user.set_password(password)
		user.save()
		return render(request,"login.html",{})

def login_data(request):
	if request.method == "POST":
		Username = request.POST['username']
		Password = request.POST['password']
		print(Username,Password)
		user = authenticate(username=Username,password=Password)
		if user is not None:
			login(request)
			return render(request,'index.html')
	return HttpResponse("Invalid Username and Password")

