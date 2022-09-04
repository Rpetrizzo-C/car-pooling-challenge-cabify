from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.models import Group
from api.serializers import LocationSerializer

class LocateAPIView(APIView):
    """
    POST to locate a group in a car
    """
    permission_classes = ()

    def post(self, request):
        data = request.data.copy()
        group_id = data['id']
        if not group_id.isdigit():
            return Response({"detail":"Incorrect group id"},status=status.HTTP_400_BAD_REQUEST)

        group = get_object_or_404(Group, id=group_id)

        if group.is_in_car():
            location = {
                'group': group.id,
                'car': group.get_car().id
            }

            return Response(
                LocationSerializer(location).data,
                status=status.HTTP_200_OK
            )
        elif group.is_already_drop_off():
            return Response({"detail":"Group not found"},status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
    