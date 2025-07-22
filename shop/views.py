# # from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Product, order
from .models import Contact,orderupdate
import random 
from django.http import HttpResponseRedirect
from django.urls import reverse
from math import  ceil
import json
def index(request):
    allproducts=[]
    catprods=Product.objects.values('category','id')
    cat={item['category'] for item in catprods }
    for cats in cat:
        pro=Product.objects.filter(category=cats)
        n = len(pro)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([pro,range(1,nSlides),nSlides,cats])
    products=Product.objects.all()
    params={
        'allproducts':allproducts,
        'products':products
        }
    return render(request, 'shop/index.html', params)
def home(request):
    return HttpResponse("this is hoe")
def about(request):
    return render(request,'shop/about.html')
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        contactno = request.POST.get('contactno', "")
        comment = request.POST.get('comment', "")
        password = request.POST.get('password', "")  # not saved in DB

        print(name, email, contactno, comment, password)
        new_contact = Contact(name=name, email=email, contactno=contactno, comment=comment,password=password)
        new_contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    message=None
    if request.method == "POST":
        orderID = request.POST.get('orderID', '').strip()
        email = request.POST.get('email', '').strip()

        try:
            # Safely convert to int
            orderID_int = int(orderID)

            # Check if order exists
            order_found = order.objects.filter(order_id=orderID_int, emailorder=email)
            # message=message = order_found.first().order_status  
            if order_found.exists():
                updates=orderupdate.objects.filter(order_id=orderID_int)
                last_update=updates.last()
                message=last_update.order_status if last_update  else "No update available"
                updates = orderupdate.objects.filter(order_id=orderID_int)
                update_list = [{'text': u.update_desc, 'time': u.timestamp} for u in updates]
                return JsonResponse({'updates': update_list, 'message': message})
            else:
                return HttpResponse("error")
        except ValueError:
            return HttpResponse("Invalid order ID (not a number)")
        except Exception as e:
            return HttpResponse(f"exception {e}")

    return render(request, 'shop/tracker.html',{'message': message})



def search(request):
   return render(request,'shop/search.html')
def prodView(request,myid):
    #sipra is fetching product from id 
    newproduct=Product.objects.filter(id=myid)
    print(newproduct)
    return render(request,'shop/productview.html', {'product': newproduct[0]})
# def checkout(request):
#     if request.method=="POST":
#       name2=request.POST.get('name2',"")
#       emailorder = request.POST.get('emailorder', "")
#       phonenumber = request.POST.get('phonenumber', "")
#       address = request.POST.get('address', "")
#       address2 = request.POST.get('address2', "")
#       city = request.POST.get('city', "")  
#       zip = request.POST.get('zip', "") 
#       famousplace=request.POST.get('famousplace'," ") 
#       state=request.POST.get('state'," ")
#       print(name2, emailorder, phonenumber, address, address2,city,zip,famousplace,state)
#         # Save tkarna ka lia DB main
#       new_order = order(name2=name2, emailorder=emailorder, phonenumber=phonenumber,city=city,zip=zip,address=address,address2=address2,famousplace=famousplace,state=state)
#       new_order.save()
#     #   new_order_id = new_order.order_id
#     #   orderupdate.objects.create(order_id=new_order.order_id, update_desc="The order has been placed")
# # shop/views.py


# # Inside your view, for example: checkout view
#       order = Order(...)  # Order is created here
#       order.save()   order_update = OrderUpdate(order=order, update_desc="Order has been placed")
#     order_update.save()

#     #   new_order = order.objects.create(...)  # Save order
#     #   update=orderupdate(order_id=new_order.id,update_desc="the order has been placed") 
#     #   update.save()  
#       new_order_id = new_order.id 
#       return redirect(f'/shop/tracker/?order_id={new_order.id}')
#     # return render(request,'shop/checkout.html')
#     # return HttpResponseRedirect(reverse('tracker') + f'?order_id={new_order.id}')
#     return render(request, 'shop/checkout.html')
def checkout(request):
    if request.method == "POST":
        name2 = request.POST.get('name2', "")
        emailorder = request.POST.get('emailorder', "")
        phonenumber = request.POST.get('phonenumber', "")
        address = request.POST.get('address', "")
        address2 = request.POST.get('address2', "")
        city = request.POST.get('city', "")  
        zip = request.POST.get('zip', "") 
        famousplace = request.POST.get('famousplace', " ") 
        state = request.POST.get('state', " ")

        new_order = order(
            name2=name2,
            emailorder=emailorder,
            phonenumber=phonenumber,
            city=city,
            zip=zip,
            address=address,
            address2=address2,
            famousplace=famousplace,
            state=state
        )
        new_order.save()
        update = orderupdate(
            order_id=new_order.order_id,
            update_desc="Order has been placed"
        )
        update.save()

        return redirect(f'/shop/tracker/?order_id={new_order.order_id}')
    
    return render(request, 'shop/checkout.html')

