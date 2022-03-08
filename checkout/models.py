import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from membership.models import Product

# Create your models here.

class CreateMembership(models.Model):
    membership_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_membership_number(self):
        """
        Generate a rendom, unique membership number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        if not self.membership_number:
            self.membership_number = self._generate_membership_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.membership_number


class MembershipNumber(models.Model):
    createmembership = models.ForeignKey(CreateMembership, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(CreateMembership, null=False, blank=False, on_delete=models.CASCADE)
    linitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.linitem_total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.createmembership.membership_number}'