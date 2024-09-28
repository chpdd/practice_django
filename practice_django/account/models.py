from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)

        user.set_password(password)

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if extra_fields.setdefault('is_staff', True) is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.setdefault('is_superuser', True) is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')

        return self.create_user(username, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=32)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    # def clean(self):
    #     pass
