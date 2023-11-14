from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    
class Vehicle(models.Model):
    owner = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=20)
    age = models.IntegerField()
    national_id = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    sensed_at = models.DateTimeField(auto_now_add=True)
    
    
class TollTransaction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)