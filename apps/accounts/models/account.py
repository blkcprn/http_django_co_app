from django.db import models
from django.conf import settings
from core.vendors import messages as msg
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
)
from core.vendors.base.model import (
    BaseModel, 
    BaseQuerySet,
)


class AccountManager(BaseUserManager):
    """Account model manager."""
    def create_user(self, username, email, password, **extra_fields):
        """Create and save a user."""
        self._check(username=username, email=email, password=password)

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Create and save a SuperUser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_valid", True)
        extra_fields.setdefault("is_blocked", False)
        extra_fields.setdefault("role", Account.Role.SU)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(msg.NOT_STAFF)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(msg.NOT_SUPERUSER)
        if extra_fields.get("is_valid") is not True:
            raise ValueError(msg.NOT_VALID)
        if extra_fields.get("is_blocked") is True:
            raise ValueError(msg.BLOCKED)
        
        return self.create_user(username, email, password, **extra_fields)
    
    def _check(self, **kwargs) -> None:
        """Check account data."""
        pass


class AdminManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Account.Role.ADMIN)


class EmployeeManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Account.Role.EMPLOYEE)


class CustomerManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Account.Role.CUSTOMER)


class GuestManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Account.Role.GUEST)


class Account(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Account model."""
    class Role(models.TextChoices):
        SU = "SU", _("Superuser")
        ADMIN = "ADMIN", _("Admin")
        EMPLOYEE = "EMPLOYEE", _("Employee")
        CUSTOMER = "CUSTOMER", _("Customer")
        GUEST = "GUEST", _("Guest")

    username = models.CharField(
        max_length=settings.LENGTH["username"]["max"],
        unique=True
    )
    email = models.EmailField(
        max_length=settings.LENGTH["email"]["max"],
        unique=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    role = models.CharField(
        max_length=10,
        choices=Role,
        default=Role.GUEST,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AccountManager.from_queryset(BaseQuerySet)()
    admin = AdminManager.from_queryset(BaseQuerySet)()
    employee = EmployeeManager.from_queryset(BaseQuerySet)()
    customer = CustomerManager.from_queryset(BaseQuerySet)()
    guest = GuestManager.from_queryset(BaseQuerySet)()

    class Meta:
        verbose_name =  _("Account")
        verbose_name_plural =  _("Accounts")
        ordering = ("-created_at",)
        permissions = [
            ("view_dashboard",   "View page: Dashboard"),
            ("change_password",  "Change account password"),
            ("allow_chat",       "Allow chat"),
        ]
        indexes = [
            models.Index(fields=["email",]),
            models.Index(fields=["username",]),
        ]

    def __str__(self):
        return self.username


class Admin(Account):
    objects = AdminManager.from_queryset(BaseQuerySet)()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.role = Account.Role.ADMIN
        super().save(*args, **kwargs)


class Employee(Account):
    objects = AdminManager.from_queryset(BaseQuerySet)()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.role = Account.Role.EMPLOYEE
        super().save(*args, **kwargs)


class Customer(Account):
    objects = AdminManager.from_queryset(BaseQuerySet)()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = Account.Role.CUSTOMER
        super().save(*args, **kwargs)


class Guest(Account):
    objects = GuestManager.from_queryset(BaseQuerySet)()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = Account.Role.GUEST
        super().save(*args, **kwargs)