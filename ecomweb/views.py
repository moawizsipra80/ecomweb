from django.http import HttpResponse
from django.shortcuts import render
def index(request):
  
    return render(request, 'index.html')
def service(request):
    return render(request,'services.html')


# def signup(request):
#     if request.method=='POST':
#        email=request.POST.get('email',' ')
#        password=request.POST.get('password',' ')
#        name=request.POST.get('name',' ')
#        contactno=request.POST.get('contactno',' ')
#        new_user=User(email=email,password=password,name=name,contactno=contactno)
#        new_user.save()
        
#        return render(request, 'signup.html', {'message': 'Account created successfully!'})
#     return render(request,'signup.html')

# def signin(request):
#     return render(request,'signin.html')