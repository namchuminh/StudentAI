from django.urls import path
from .views import Index, ClassSubject, ScoresSubject


urlpatterns = [
    path("", Index.as_view(), name='index_scores'),
    path("<slug:slug>/", ClassSubject.as_view(), name='class_subject'),
    path("<slug:slug_subject>/<slug:slug_class>/", ScoresSubject.as_view(), name='scores_subject'),
]