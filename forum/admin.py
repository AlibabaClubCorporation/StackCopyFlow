from django.contrib import admin

from mptt.admin import MPTTModelAdmin 

from .models import *



@admin.register( Label )
class LabelAdmin( admin.ModelAdmin ):
    """
        Label model class for admin panel
    """

    list_display = ( 'name', 'creator',)

@admin.register( Question )
class QuestionAdmin( admin.ModelAdmin ):
    """
        Question model class for admin panel
    """

    list_display = ( 'title', 'date_of_creation', 'creator', )
    list_filter = ( 'title', 'date_of_creation', )
    readonly_fields = ( 'date_of_creation', )

    fieldsets = (
        ( 'General', {
            'fields' : ( ( 'title', ), ( 'date_of_creation', 'creator', ), )
        }),

        ( 'Additionaly', {
            'classes' : ( 'collapse', ),
            'fields' : ( ( 'content', ), ( 'labels', ), )
        })
    )

@admin.register( Answer )
class AnswerAdmin( MPTTModelAdmin ):
    """
        Answer model class for admin panel
    """

    list_display = ( 'date_of_creation', 'creator', 'question' )
    list_filter = ( 'date_of_creation', )
    readonly_fields = ( 'date_of_creation', )

    fieldsets = (
        ( 'General', {
            'fields' : ( ( 'date_of_creation', ), ( 'question', 'creator', ), )
        }),

        ( 'Additionaly', {
            'classes' : ( 'collapse', ),
            'fields' : ( ( 'content', ), ( 'parent', ), )
        }),
    )

@admin.register( Rating )
class RatingAdmin( admin.ModelAdmin ):
    """
        Rating model class for admin panel
    """

    list_display = ( 'user', 'rating', 'content_type', 'content_object', 'object_pk' )