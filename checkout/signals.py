from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import MembershipNumber

@receiver(post_save, sender=MembershipNumber)
def update_on_save(sender, instance, created, **kwargs):
    """
    update memebership total on MembershipNumber
    """
    instance.order.update_total()

@receiver(post_save, sender=MembershipNumber)
def update_on_save(sender, instance, **kwargs):
    """
    update memebership total on MembershipNumber
    """
    instance.order.update_total()