from main.models import Network
from rest_framework import serializers


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['essid', 'bssid', 'password', 'status', 'file']


class NetworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['essid', 'bssid']
