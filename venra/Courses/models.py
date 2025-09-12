from django.db import models
from UserAuth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Courses(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name="courses")
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    units = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.code
 
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    level = models.PositiveIntegerField(default=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
    
    @property
    def courses(self):
        if self.department:
            return self.department.courses.all()
        return []
    