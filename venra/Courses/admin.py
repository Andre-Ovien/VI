from django.contrib import admin
from .models import Profile, Courses, Department

# Register your models here.

admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Department)