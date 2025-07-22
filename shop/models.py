from django.utils import timezone
from django.db import models
class  Product(models.Model):
    product_id=models.AutoField
    name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=1200)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    pro_date=models.DateField(default=timezone.now)
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
       return self.name
    
class checkout(models.Model):
    checkout_amount=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f" {self.id} -RS {self.checkout_amount}"
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100, default=" ")
    comment = models.CharField(max_length=500, default=" ")
    contactno = models.CharField(max_length=100, default=" ")
    password = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name

class order(models.Model):
    order_id = models.AutoField(primary_key=True)  # <-- Add this
    emailorder=models.CharField(max_length=100,default=" ")
    name2=models.CharField(max_length=100,default=" ")
    phonenumber=models.CharField(max_length=15,default=" ")
    address=models.CharField(max_length=500,default=" ")
    address2=models.CharField(max_length=500,default=" ")
    famousplace=models.CharField(max_length=300,default=" ")
    state=models.CharField(max_length=30,default=" ")
    city=models.CharField(max_length=30,default=" " )
    zip=models.CharField(max_length=10,default=" ")
    def __str__(self):
     return self.name2    

class orderupdate(models.Model):
    order_id = models.IntegerField(default=0)  
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=200,default=" ")

def __str__(self):
    return self.update_desc[0:7]+"..."