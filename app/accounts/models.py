from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class AccountManager(BaseUserManager):
    def create_account(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        account_obj = self.model (
            email = self.normalize_email(email)
        )
        account_obj.set_password(password)
        account_obj.active = is_active
        account_obj.admin = is_admin
        account_obj.staff = is_staff
        account_obj.save(using=self._db)
        return account_obj

    def create_staffuser(self, email, password=None):
        account = self.create_account (
            email,
            password=password,
            staff = True
        )
        return account

    def create_superuser(self, email, password=None):
        account = self.create_account (
            email,
            password=password,
            staff = True,
            admin = True
        )
        return account

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    phone = models.IntegerField(unique=True, null=True)
    full_name = models.CharField(max_length=230, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
