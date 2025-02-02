from django.contrib import admin
from .models import twoDo

# Register your models here.

class twoDoModel(admin.ModelAdmin):
    list_display = ('title', 'date_created')

admin.site.register(twoDo, twoDoModel)