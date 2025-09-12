from django.shortcuts import render
from rest_framework.viewsets import generics
from .models import Courses, Department, Profile
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import CourseSerializer, DepartmentSerializer, ProfileSerializer
from UserAuth.models import User

# Create your views here.

class ListCreateCourseApiView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class ListCreateDepartmentApiview(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class ProfileCreateApiView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)