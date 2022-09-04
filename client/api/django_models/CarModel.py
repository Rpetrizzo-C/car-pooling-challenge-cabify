from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, transaction
from django.utils import timezone

import api.models 

class Car(models.Model):
    """
    Car for journeys
    """
    created = models.DateTimeField(default=timezone.now)
    seats = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(4), MaxValueValidator(6)]
    )
    is_available = models.BooleanField(default=True)

    def get_available_group(self):
        """
        Detect a available group

        :returns: Available group
        :type returns: journey.Group
        """
        return api.models.Group.objects.filter(
            people__lte=self.seats,
            is_available=True
        ).order_by('people', 'created').first()
