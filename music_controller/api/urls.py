from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomView.as_view(), name='room_view'),
    path('create-room', views.CreateRoomView.as_view(), name='create_room_view'),
    path('get-room', views.GetRoom.as_view())
]