from django.contrib import admin
from .models import TodoItem, Vehicle

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Vehicle)