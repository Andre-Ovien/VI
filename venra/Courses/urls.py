from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.ListCreateCourseApiView.as_view(), name="courses"),
    path('departments/',views.ListCreateDepartmentApiview.as_view(), name="departments"),
    path('profile/',views.ProfileCreateApiView.as_view(), name="profile"),
]