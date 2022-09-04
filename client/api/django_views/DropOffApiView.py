from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.models import Group
from api.utils import get_available_group

class DropOffAPIView(APIView):
    """
    POST drop off a group
    """
    permission_classes = ()

    def post(self, request):
        data = request.data.copy()
        group_id = data['id']
        if not group_id.isdigit():
            return Response({"detail":"Incorrect group id"},status=status.HTTP_400_BAD_REQUEST)
        
        group = get_object_or_404(Group, id=group_id)
        group.finish_journey()

        if hasattr(group, 'journey'):
            get_available_group(group.journey.car)
        return Response(status=status.HTTP_200_OK)
