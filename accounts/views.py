from email import message
from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect

# from .models import HttpResponse
def signup(request):
    if request.method=='POST':
       email=request.POST.get('email',' ')
       password=request.POST.get('password',' ')
       name=request.POST.get('name',' ')
       contactno=request.POST.get('contactno',' ')
       new_user=User(email=email,password=password,name=name,contactno=contactno)
       new_user.save()
        
       return render(request, 'accounts/signup.html', {'message': 'Account created successfully!'})
    return render(request,'accounts/signup.html')
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email, password=password).first()
        if user:
            return redirect('/shop/')
        else:
            return render(request, 'accounts/signin.html', {'error': 'Invalid credentials'})
            
    return render(request, 'accounts/signin.html')
    # return render(request,'signin.html ')
# Create your views here.
