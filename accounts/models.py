from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,number,password):
        if not number:
            raise ValueError('Number Is Not There !')
        user = self.model(number=number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,number,password):
        user = self.create_user(number,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    number = models.CharField(max_length=11,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'number'
    objects = UserManager()

    def __str__(self):
        return f"{self.number} - {self.is_superuser}"