from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     is_customer= models.BooleanField(default=False)
#     is_employee= models.BooleanField(default=False)
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=255)

# class Employee(models.Model):
#     pass



class Customer(models.Model):
    user = models.CharField(max_length=255)
    # user = models.OneToOneField(User,on_delete=models.CASCADE,default=True)
    age = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    nationality = models.CharField(max_length=155)
    country = models.CharField(max_length=255)
    check_in = models.DateTimeField(auto_now=False)
    check_out = models.DateTimeField(auto_now=False)


    def __str__(self):
        return self.user




class Room(models.Model):
    room_status=(
        ("av","available"),
        ("bk","booked"),)
    room_name = models.CharField(max_length=255,default=True)
    room_number = models.CharField(max_length=255,) # onetoone relationship with User
    room_type = models.CharField(max_length=255) # choice filed will be include
    price_pernight = models.CharField(max_length=255)
    max_person = models.IntegerField()
    room_description = models.CharField(max_length=500,)
    booking_timeframe = models.CharField(max_length=500)


    status = models.CharField(max_length=255,choices=room_status,default="av")

    def __str__(self):
        return f" {self.room_name} own room {self.room_number} "



class Booked(models.Model):

    customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    room_number= models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.customer_name.user}'


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Kitchen_items(models.Model):
    product_name= models.CharField(max_length=255)
    price = models.FloatField(max_length=1000)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    qty = models.FloatField(max_length=255)


    def __str__(self):
        return self.product_name


class Bar_items(models.Model):
    product_name= models.CharField(max_length=255)
    price = models.FloatField(max_length=1000)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    qty = models.FloatField(max_length=255)



    def __str__(self):
        return self.product_name



class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    kitchen_item = models.ManyToManyField(Kitchen_items)
    bar_items = models.ManyToManyField(Bar_items)
    qty = models.FloatField(max_length=255,null=True)
    total = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.customer.user



