from django.urls import path
from main.views import NetworkListCreate, crack_network


urlpatterns = [
    path('networks/', NetworkListCreate.as_view()),
    path('networks/crack/<str:bssid>/', crack_network),
]