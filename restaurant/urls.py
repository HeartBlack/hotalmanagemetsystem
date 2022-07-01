from unicodedata import name
from django.urls import path,include
from .views import *
urlpatterns = [
  
    path("customers_list/" ,customer_list,name="customer_list"),

    path("room_list/",room_list,name="room_list"),
    path("create_room/" ,create_room,name="create_room"),

    path("available_room_list/",available_room_list,name="available_room_list"),

    path("booking_reservation/",booking_reservation,name="booking_reservation"),


    # categories links
    path("list_category/",list_category,name="list_category"),
    path("create_category/",create_category,name="create_category"),


    # Kitchen items url
    path("list_kitchen_items/",list_Kitchen_items,name="list_Kitchen_items"),
    path("create_kitchen_items/",create_Kitchen_items,name="create_Kitchen_items"),



    # bar items url
    path("list_bar_items/",list_bar_items,name="list_bar_items"),
    path("create_bar_items/",create_bar_items,name="create_bar_items"),




]
