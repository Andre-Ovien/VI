from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be a staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Must be a Superuser')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=253, blank=True, null=True)

    is_staff = models.BooleanField(
        gettext_lazy('Staff Status'), default=False,
        help_text= gettext_lazy('Designates whether the user can log in the site')
    )
    is_active = models.BooleanField(
        gettext_lazy('Active Status'), default=True,
        help_text= gettext_lazy('Designates whether this user should be treated as active')
    )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email