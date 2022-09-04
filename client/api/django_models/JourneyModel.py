from django.db import models, transaction
from django.utils import timezone

class Journey(models.Model):
    """
    Journey of a group in a specific car
    """
    started = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(null=True, blank=True)
    group = models.OneToOneField(
        'Group',
        related_name='journey',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='journeys'
    )

    def get_car(self):
        return self.car

    @transaction.atomic
    def finish(self):
        """
        Finish the journey
        """
        self.finished = timezone.now()
        self.car.is_available = True
        self.car.save()
        self.save()
