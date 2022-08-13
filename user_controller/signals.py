from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ComplaintToUser
from .services.service_of_complaint import UserBannedController



@receiver( post_save, sender = ComplaintToUser )
def check_auto_banned( sender, instance, created, **kwargs ):
    if ComplaintToUser.objects.filter( receiver = instance.receiver ).count() > 4:
        UserBannedController.user_blocking( instance.receiver )