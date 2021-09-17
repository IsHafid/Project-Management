from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display=['name','team']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['T_name','Project_name','user']
    prepopulated_fields={'slug':('T_name',)}

@admin.register(P_category)
class P_CategoryAdmin(admin.ModelAdmin):
    list_display=['name',]
    prepopulated_fields = {'slug':('name',)}

