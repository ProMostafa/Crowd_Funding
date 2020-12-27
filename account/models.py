from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.core.validators import RegexValidator
from django.contrib import messages


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email or not last_name or not first_name or not phone:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    # mobile = models.CharField(max_length=11, blank=False)
    phone_regex = RegexValidator(regex=r'^01(0|1|2|5)[0-9]{8}$',
                                 message="Phone number must be entered in the format: '01099999999'. Up to 11 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)

    avatar = models.ImageField(upload_to='avatars/', blank=True)
    country = models.CharField(max_length=70, blank=True)
    fb_account = models.URLField(max_length=120, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
