from rest_framework import serializers
from .models import Courses, Department, Profile
from UserAuth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'name',
        )


class CourseSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name',read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset = Department.objects.all(),
        source="department",
        write_only=True
    )
    class Meta:
        model = Courses
        fields = (
            'id',
            'department',
            'department_id',
            'code',
            'title',
            'units',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    department_name = serializers.CharField(source="department.name", read_only=True)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "level",
            "department",
            "department_name",
            "courses",
        ]
        extra_kwargs = {
            "department": {"write_only": True}  
        }
