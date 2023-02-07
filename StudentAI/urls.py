from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import Index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('', include('user.urls')),
    path('sinh-vien/', include('students.urls')),
    path('mon-hoc/', include('subjects.urls')),
    path('diem-so/', include('scores.urls')),
    path('diem-danh/', include('attendance.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
