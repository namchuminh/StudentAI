from django.urls import path
from .views import Attendance, video_feed, CropFace, AttendanceInformation, SelectAttendance

urlpatterns = [
    path("", Attendance.as_view(), name='attendance_students'),
    path("thong-tin-diem-danh/", AttendanceInformation.as_view(), name='attendance_information_students'),
    path("tao-khuan-mat/", CropFace.as_view(), name='cropface_students'),
    path('video_feed/', video_feed, name="video-feed"),
    path('chon-mon/', SelectAttendance.as_view(), name='select_attendance')
]