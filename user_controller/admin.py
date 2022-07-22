from django.contrib import admin

from .models import *

# Register your models here.

@admin.register( CustomUser )
class CustomUserAdmin( admin.ModelAdmin ):
    """
        User custom model class for admin panel
    """

    list_display = ( 'username', 'registration_date', 'first_name', 'last_name', 'gender', 'birth_date' )
    list_filter = ( 'registration_date', )
    readonly_fields = ( 'registration_date', )

    fieldsets = (
        ( 'Общее', {
            'fields' : ( ( 'username', ), ( 'registration_date' ), )
        }),

        ( 'О пользователе', {
            'classes' : ( 'collapse', ),
            'fields' : ( ('first_name', 'last_name'), 'gender', 'birth_date' )
        })
    )