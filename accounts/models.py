from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):

     def create_user(self, first_name, last_name,username,phone, email,password=None):

       user = self.model(
           email=self.normalize_email(email),
           first_name=first_name,
           last_name=last_name,
           username=username,
           phone=phone
            )
       user.is_admin = False
       user.is_superuser = False
       user.is_staff = False
       user.is_active = True
       user.set_password(password)
       user.save(using=self._db)
       return user

     def create_superuser(self, first_name, last_name,username,phone, email,password=None):

       user = self.model(
           email=self.normalize_email(email),
           first_name=first_name,
           last_name=last_name,
           username=username,
           phone=phone
            )
       user.is_admin = True
       user.is_superuser = True
       user.is_staff = True
       user.is_active = True
       user.set_password(password)
       user.save(using=self._db)
       return user


from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
    RULE_CHOICES = [
        ('customer', 'Customer'),
        ('provider', 'Provider'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    rule = models.CharField(max_length=100, choices=RULE_CHOICES, blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone']
    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


