from django.shortcuts import render

# Create your views here.

from main.models import Network
from main.serializers import NetworkSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pathlib import Path

import os, subprocess


class NetworkListCreate(generics.ListCreateAPIView):
    queryset = Network.objects.all()  # filter(status="cracked")
    serializer_class = NetworkSerializer


@api_view(['GET'])
def crack_network(request, bssid):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        try:
            network = Network.objects.get(bssid=bssid)
            print("\n\n\nOn est laaaaaaa : bssid = {}".format(bssid))
            print("On est laaaaaaa : network = {}\n\n\n".format(network))
            serializer = NetworkSerializer(network)

            BASE_DIR = Path(__file__).resolve().parent.parent
            scripts_dir = os.path.join(BASE_DIR, 'scripts')
            subprocess.call(scripts_dir + '/test.sh')
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Network.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
