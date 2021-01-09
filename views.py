from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
	return HttpResponse("hellow You are at the Customer Section...Thanks")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form':form})
	

def login(request):
	if request.method== 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
	else:
		return render(request, 'login.html')
	
	'''	if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('/login')'''
	
