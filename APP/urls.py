from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # Room Type
    path('room-type-list', views.RoomTypeView.list, name="room_type_list"),
    path('room-type-add', views.RoomTypeView.create, name="room_type_add"),
    path('room-type-save', views.RoomTypeView.save, name="room_type_save"),
    path('room-type-edit/<id>', views.RoomTypeView.edit, name="room_type_edit"),
    path('room-type-update', views.RoomTypeView.update, name="room_type_update"),
    path('room-type-delete/<int:id>', views.RoomTypeView.delete, name="room_type_delete"),

    # Room
    path('room-list', views.RoomView.index, name="room_list"),
    path('get-room-list', views.RoomView.get_room_list, name="get_room_list"),
    path('get-room-by-id/<id>', views.RoomView.get_room_by_id, name="get_room_by_id"),
]
