from django.db import models


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=50)
    name_kh = models.CharField(max_length=50)
    objects = models.Manager

    class Meta:
        db_table = "tbl_room_type"
class Building(models.Model):
    name = models.CharField(max_length=50)
    name_kh = models.CharField(max_length=50)
    objects = models.Manager

    class Meta:
        db_table = 'tbl_building'
class Floor(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_no = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    objects = models.Manager

    class Meta:
        db_table = 'tbl_floor'

class Room(models.Model):
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=20)
    service_charge = models.FloatField()
    price = models.FloatField()
    room_key = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    note = models.CharField(max_length=100)
    objects = models.Manager

    class Meta:
        db_table = 'tbl_room'