from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseRedirect

class IndexAPIView(APIView):
    """
    GET redirects to status/
    """
    permission_classes = ()

    def get(self, request):
        return HttpResponseRedirect('status')


