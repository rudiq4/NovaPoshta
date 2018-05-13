from django.db import models


class Cargo(models.Model):
    weight = models.PositiveIntegerField()
    bulk_weight = models.PositiveIntegerField()
    acceptance_adress = models.ForeignKey()
    destination_adress = models.ForeignKey()
    packaging = models.ForeignKey(Packaging, blank=True, default=None)



class Packaging(models.Model):
    PACKAGE_CHOICE = (
        ('B', 'BOX'),
        ('S', 'STRATCH')
    )
    package = models.CharField(
        max_length=1,
        choices=PACKAGE_CHOICE,
        blank=True
    )
    price = models.PositiveIntegerField()