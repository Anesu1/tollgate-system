from django.shortcuts import render, HttpResponse
from .models import TodoItem, Vehicle

# Create your views here.

def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, "details.html", {"vehicles": vehicles})


def sense_vehicle(request):
    if request.method == 'POST':
        # Simulate vehicle sensing using a POST request
        plate_number = request.POST.get('plate_number')
        owner = request.POST.get('owner')
        age = request.POST.get('age')
        national_id = request.POST.get('national_id')
        address = request.POST.get('address')

        # Create a new Vehicle instance
        vehicle = Vehicle(
            owner=owner,
            plate_number=plate_number,
            age=age,
            national_id=national_id,
            address=address
        )
        vehicle.save()  # Save the vehicle information to the database

        return HttpResponse(f"Vehicle with plate number {plate_number} sensed successfully.")

    return render(request, 'sensing.html')