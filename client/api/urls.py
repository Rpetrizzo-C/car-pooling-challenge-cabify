from django.contrib import admin
from django.urls import path

from .views import (
        StatusAPIView,CarAPIView,JourneyAPIView,
        DropOffAPIView,LocateAPIView,IndexAPIView
)


urlpatterns = [
    path(
        '',
        IndexAPIView.as_view(),
        name='index'
    ),
    path(
        'status/',
        StatusAPIView.as_view(),
        name='get_status'
    ),
    path(
        'cars/',
        CarAPIView.as_view(),
        name='put_cars'
    ),
    path(
        'journey/',
        JourneyAPIView.as_view(),
        name='post_journey'
    ),
    path(
        'dropoff/',
        DropOffAPIView.as_view(),
        name='post_dropoff'
    ),
    path(
        'locate/',
        LocateAPIView.as_view(),
        name='post_locate'
    ),
]
