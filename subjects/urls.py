from django.urls import path
from .views import ListSubjects, CreateSubjects, UpdateSubjects

urlpatterns = [
    path("", ListSubjects.as_view(), name='list_subjects'),
    path("them/", CreateSubjects.as_view(), name='create_subjects'),
    path("sua/<int:pk>", UpdateSubjects.as_view(), name='update_subjects'),
]