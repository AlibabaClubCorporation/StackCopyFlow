from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import *



@receiver( post_save, sender = CustomUser )
def assigning_group_to_user( sender, instance, created, **kwargs ):
    instance.groups.add( Group.objects.get( name = 'user' ) )