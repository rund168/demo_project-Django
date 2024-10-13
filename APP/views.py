from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Room
from .models import RoomType


def home(request):
    return render(request, 'home.html')


class RoomTypeView:

    def list(request):
        data = RoomType.objects.all()
        context = {
            'data': data
        }
        return render(request, "RoomType/index.html", context)

    def create(request):
        return render(request, 'RoomType/create.html')

    def edit(request, id):
        data = RoomType.objects.get(id=id)
        context = {
            'data': data
        }
        return render(request, "RoomType/update.html", context)

    def save(request):
        if request.method != 'POST':
            messages.error(request, "Invalid Method!")
            return redirect('room_type_add')
        else:
            try:
                name = request.POST.get('name')
                name_kh = request.POST.get('name_kh')

                room_Type_model = RoomType(name=name, name_kh=name_kh)
                room_Type_model.save()
                messages.success(request, 'Room Type has been created!')
                return redirect('room_type_list')
            except:
                messages.error(request, 'Something went wrong!')
                return redirect('room_type_add')

    def update(request):
        if request.method != 'POST':
            messages.error(request, "Invalid Method!")
            return redirect('room_type_add')
        else:
            try:
                id = request.POST.get('id')
                name = request.POST.get('name')
                name_kh = request.POST.get('name_kh')

                data = RoomType.objects.get(id=id)
                if data is not None:
                    data.name = name
                    data.name_kh = name_kh
                    data.save()
                    messages.success(request, 'Room Type has been created!')
                    return redirect('room_type_list')
            except:
                messages.error(request, 'Something went wrong!')
                return redirect('room_type_add')

    def delete(request, id):
        if request.method != 'POST':
            messages.error(request, "Invalid Method!")
            return redirect('room_type_list')  # Redirect to list view if method is not POST

        try:
            room_type = RoomType.objects.get(id=id)  # Get the RoomType object by id
            room_type.delete()  # Delete the object from the database
            messages.success(request, 'Room Type has been deleted successfully!')
        except RoomType.DoesNotExist:
            messages.error(request, 'Room Type not found!')
        except Exception as e:
            messages.error(request, f'Something went wrong: {e}')

        return redirect('room_type_list')


class RoomView(View):
    def index(request):
        data = Room.objects.all()
        context = {
            'data': data
        }
        return render(request, 'Room/index.html', context)


def get_room_by_id(request, id):
    data = Room.objects.get(id=id)
    context = {
        'id': data.id,
        'room_type': data.room_type_id,
        'floor': data.floor_id,
        'room_no': data.room_no,
        'service_charge': data.service_charge,
        'price': data.price,
        'room_key': data.room_key,
        'status': data.status,
        'note': data.note
    }
    return JsonResponse({'data': context})
