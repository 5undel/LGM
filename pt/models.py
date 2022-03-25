from django.db import models


# to categoris the memberships
class TraningCategory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# To create the diffrent membership
class Coach(models.Model):
    TIME_CHOICE = (
        (0, '14:00-15:00'),
        (1, '16:00-17:00'),
        (2, '20:00-21:00'),
    )

    category = models.ForeignKey('TraningCategory', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    time = models.CharField(max_length=10, null=True,
                            blank=True, choices=TIME_CHOICE)

    def __str__(self):
        return self.name
