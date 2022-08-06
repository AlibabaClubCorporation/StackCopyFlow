from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import AppealToUser



@receiver( post_save, sender = AppealToUser )
def check_auto_banned( sender, instance, created, **kwargs ):
    if AppealToUser.objects.filter( receiver = instance.receiver ).count() > 4:
        instance.receiver.groups.clear()
        instance.receiver.groups.add( Group.objects.get( name = 'banned' ) )