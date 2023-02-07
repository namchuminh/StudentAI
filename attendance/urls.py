from django.urls import path
from .views import Attendance, video_feed, CropFace

urlpatterns = [
    path("", Attendance.as_view(), name='attendance_students'),
    path("tao-khuan-mat/", CropFace.as_view(), name='cropface_students'),
    path('video_feed/', video_feed, name="video-feed")
]