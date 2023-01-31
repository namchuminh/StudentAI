from django.urls import path
from .views import ListStudents, CreateStudents, UpdateStudents, Delete_Students, export_students_xls

urlpatterns = [
    path("", ListStudents.as_view(), name='list_students'),
    path("them/", CreateStudents.as_view(), name='create_students'),
    path("sua/<int:pk>", UpdateStudents.as_view(), name='update_students'),
    path("xoa/<int:pk>", Delete_Students.as_view(), name='delete_students'),
    path("xuat/", export_students_xls, name='export_students'),
]