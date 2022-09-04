from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, transaction
from django.utils import timezone

from api.exceptions import AssignCarException, JourneyException
import api.models

class Group(models.Model):
    """
    Group of people that want a journey
    """
    created = models.DateTimeField(default=timezone.now)
    people = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(4), MaxValueValidator(6)]
    )
    is_available = models.BooleanField(default=True)

    def is_already_drop_off(self):
        """
        Detect if the group is already drop off

        :returns: if group alredy drop off
        :type returns: Bool
        """
        if (
            not self.is_available and
            hasattr(self, 'journey') and
            self.journey.finished
        ):
            return True
        return False

    def is_in_car(self):
        """
        Detect if the group is in a car

        :returns: if group is in a car
        :type returns: Bool
        """
        if (
            not self.is_available and
            hasattr(self, 'journey') and
            not self.journey.finished
        ):
            return True
        return False

    def get_car(self):
        """
        Return the car assigned to the group

        :returns: car assigned
        :type returns: journey.Car
        """
        if self.is_in_car() or self.is_already_drop_off():
            return self.journey.get_car()
        return None

    def get_available_car(self):
        """
        Get a available car for the group

        :returns: a available car
        :type returns: journey.Car
        """
        if self.is_in_car() or self.is_already_drop_off():
            raise JourneyException("Group {} is in a car or "
                                   "finished journey".format(self.id))

        return api.models.Car.objects.filter(
            seats__gte=self.people,
            is_available=True
        ).order_by('seats').first()

    @transaction.atomic
    def assign_car(self, car):
        """
        Start a journey assigning a car to the group

        :param car: Car to assign to the group
        :type car: journey.Car
        """
        if self.is_in_car() or self.is_already_drop_off():
            raise JourneyException("Group {} is in a car or "
                                   "finished journey".format(self.id))

        if not(self.is_available and
               car.is_available and
               self.people <= car.seats):
            raise AssignCarException("Imposible to assign group "
                                     "{} to car {}".format(self.id, car.id))

        api.models.Journey.objects.create(group=self, car=car)
        car.is_available = False
        car.save()
        self.is_available = False
        self.save()

    @transaction.atomic
    def finish_journey(self):
        """
        Finish a journey of a group
        """
        if self.is_in_car():
            self.journey.finish()

        self.is_available = False
        self.save()

