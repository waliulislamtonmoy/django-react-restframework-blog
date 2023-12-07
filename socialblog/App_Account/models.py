from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class UserProfileManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email not found")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields

        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("In SuperUser is_staff must be true")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("In SuperUser is_superuser must be true")
        return self.create_user(email=email, password=password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    fullname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="profileimage/", blank=True,null=True)
    address = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
