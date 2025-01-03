"""
Custom user model (Account).
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from core.vendors.base.model import (
    Usable,
    BaseModel,
)


class AccountManager(BaseUserManager):
    def create_user(
        self, username: str, email: str, password: str | None = None
    ):
        """Creates and saves a user with the username, email, password."""

        # check user data
        self._check(username=username, email=email, password=password)

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username: str, email: str, password: str | None = None
    ):
        """
        Creates and saves a superuser with the username,
        email, password.
        """

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def _check(self, **kwargs) -> None:
        """Check user data."""
        pass


class Account(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=80, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def is_usable(self, **kwargs) -> Usable:
        """Check account, is_active, is_confirmed are True."""
        pass
