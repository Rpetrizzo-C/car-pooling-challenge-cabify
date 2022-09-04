from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.models import Group
from api.utils import request_available_car,process_journey_payload

class JourneyAPIView(APIView):
    """
    POST a new request of a journey
    """
    permission_classes = ()

    def post(self, request):
        group = process_journey_payload(request.data)
        if Group.objects.filter(id=group.id).exists():
            return Response({"detail":"Group id already in use"},status=status.HTTP_400_BAD_REQUEST)

        try:
            group.save()
        except Exception as e:
            return Response({"detail":f"Exception: {e}"},status=status.HTTP_400_BAD_REQUEST)

        request_available_car(group)
        return Response(status=status.HTTP_200_OK)
