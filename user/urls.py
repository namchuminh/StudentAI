from django.urls import path
from .views import Login, Home, Logout, Profile

urlpatterns = [
    path("dang-nhap/", Login.as_view(), name='login'),
    path("dang-xuat/", Logout.as_view(), name='logout'),
    path("trang-chu/", Home.as_view(), name='home'),
    path("ca-nhan/", Profile.as_view(), name='profile'),
]