
from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import Customer,Room,Booked,Category,Kitchen_items,Bar_items



class CustomerSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"




class RoomBookedSerializer(serializers.ModelSerializer):
    customer_name = CustomerSeriallizer()
    room_number = RoomListSerializer()
    class Meta:
        model = Booked
        fields =[ "customer_name","room_number"]



class CategoriesSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class KitchenItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen_items
        fields = "__all__"



class BarItemsseriallizer(serializers.ModelSerializer):
    class Meta:
        model = Bar_items
        fields = "__all__"