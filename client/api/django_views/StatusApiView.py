from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class StatusAPIView(APIView):
    """
    GET status of the system
    """
    permission_classes = ()

    def get(self, request):
        return Response({'status': "200 OK"},status=status.HTTP_200_OK)
