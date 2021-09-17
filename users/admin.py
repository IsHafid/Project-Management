from django.contrib import admin

# Register your models here.
from .models import Statut, UsersBase



@admin.register(UsersBase)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['CIN','slug']
    prepopulated_fields = {'slug':('CIN','lastname','firstname')}


@admin.register(Statut)
class StatutAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}