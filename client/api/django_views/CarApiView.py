from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.models import Car
from api.utils import clean_system, process_cars_payload

class CarAPIView(APIView):
    """
    PUT to add new cars
    """
    permission_classes = ()

    def put(self, request):
        cars = process_cars_payload(request.data)
        clean_system()

        try:
            Car.objects.bulk_create(cars)
        except Exception:
            return Response({"detail":"Incorrect payload"},status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
