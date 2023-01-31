from django.contrib import admin
from .models import Students, ClassName, Specialization
# Register your models here.
admin.site.register(Students)
admin.site.register(ClassName)
admin.site.register(Specialization)