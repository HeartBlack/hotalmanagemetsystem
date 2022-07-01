from django.shortcuts import render
from yaml import serialize
# Create your views here.
from .models import Booked, Category, Customer, Kitchen_items,Room,Bar_items
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSeriallizer,RoomListSerializer,RoomBookedSerializer,CategoriesSeriallizer,KitchenItemsSerializer,BarItemsseriallizer


@api_view(['GET'])
def customer_list(request):
    customer = Customer.objects.all()
    serializer = CustomerSeriallizer(customer,many=True)

    return Response(serializer.data)




@api_view(["POST"])
def create_room(request):
    if request.method == "POST":
        serializer = RoomListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"messgae":"Room is create"})



@api_view(['GET'])
def room_list(request):
    room = Room.objects.all()
    serializer = RoomListSerializer(room,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def available_room_list(request):
    available = Room.objects.filter(status="av")
    serializer = RoomListSerializer(available,many=True)
    return Response(serializer.data)




@api_view(["GET","POST"])
def booking_reservation(request):
    booked = Booked.objects.all()
    serializer = RoomBookedSerializer(booked,many=True)
    return Response(serializer.data)




@api_view(["GET"])
def list_category(request):
    categories = Category.objects.all()
    serializer = CategoriesSeriallizer(categories,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_category(request):
    if request.method== "POST":
        serializer = CategoriesSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response({"message":"categories added successfully"})




@api_view(["GET"])
def list_Kitchen_items(request):
    kitchen_items = Kitchen_items.objects.all()
    serializer = KitchenItemsSerializer(kitchen_items,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_Kitchen_items(request):
    if request.method== "POST":
        serializer = KitchenItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response({"message":"Kitchen items added successfully"})



@api_view(["GET"])
def list_bar_items(request):
    bar_items = Bar_items.objects.all()
    serializer = BarItemsseriallizer(bar_items,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_bar_items(request):
    if request.method== "POST":
        serializer = BarItemsseriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response({"message":"Kitchen items added successfully"})





