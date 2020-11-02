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
            is_server_busy = Network.objects.filter(status="pending").count() > 0

            if is_server_busy:
                return Response("Our server is already busy", status=status.HTTP_400_BAD_REQUEST)
            else:
                network = Network.objects.get(bssid=bssid)
                serializer = NetworkSerializer(network)

                if network.status == 'not_cracked':
                    network.status = "pending"
                    network.save()
                    thread = BruteForceThread(network)
                    thread.start()

                return Response(serializer.data, status=status.HTTP_200_OK)

        except Network.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
