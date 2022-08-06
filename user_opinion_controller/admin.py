from django.contrib import admin

from .models import Rating

# Register your models here.

@admin.register( Rating )
class RatingAdmin( admin.ModelAdmin ):
    """
        Rating model class for admin panel
    """

    list_display = ( 'user', 'rating', 'content_type', 'content_object', 'object_pk' )