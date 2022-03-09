from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import MembershipNumber

@receiver(post_save, sender=MembershipNumber)
def update_on_save(sender, instance, created, **kwargs):
    """
    update memebership total on MembershipNumber
    """
    instance.createmembership.update_total()

@receiver(post_save, sender=MembershipNumber)
def update_on_delete(sender, instance, **kwargs):
    """
    update memebership total on MembershipNumber
    """
    print('delete signal receiver!')
    instance.createmembership.update_total()