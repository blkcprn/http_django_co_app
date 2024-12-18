from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone
from .filter import ArchivedFilter
from django.http import HttpRequest 
from django.db.models import QuerySet
from core.vendors import messages as msg
from ..mixins.model import ExportAsCSVMixin
from django.utils.translation import gettext_lazy as _
from typing import (
    Tuple,
    List,
    Dict,
)


class BaseQuerySet(models.QuerySet):
    """Base queryset."""
    def valid(self, valid: bool = True):
        return self.filter(is_valid=valid)
    
    def blocked(self, blocked: bool = True):
        return self.filter(is_blocked=blocked)
    
    def archived(self, archived: bool = True):
        return self.filter(archived_at__isnull=archived)
    
    def actual(self, valid: bool = True, blocked: bool = False):
        return self.filter(is_valid=valid, is_blocked=blocked)
    
    def usable(self, valid: bool = True, blocked: bool = False, archived: bool = False):
        return self.filter(is_valid=valid, is_blocked=blocked, archived_at__isnull=not archived)


class BaseModel(models.Model):
    """Base model class."""
    is_valid = models.BooleanField(
        default=False
    )
    is_blocked = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    archived_at = models.DateTimeField(
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        "accounts.Account",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_creator",
    )
    updater = models.ForeignKey(
        "accounts.Account",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updater",
    )

    objects = BaseQuerySet.as_manager()
    
    @property
    def archived(self) -> bool:
        """Get if is archived."""
        return self.archived_at is None
    
    @archived.setter
    def archived(self, val: bool) -> None:
        """Set archived_at. If val is true, is_valid set False, is_blocked set True."""
        self.archived_at = timezone.now() if val is True else None
        self.usable = not val
    
    @property
    def actual(self) -> bool:
        """Get check: is_valid is True and is_blocked is False."""
        return self.is_valid is True and self.is_blocked is False
    
    @actual.setter
    def actual(self, val: bool) -> None:
        """Set valid, blocked, archived."""
        self.is_valid = val
        self.is_blocked = not val
    
    @property
    def usable(self) -> bool:
        """Get check: is_valid is True and is_blocked is False."""
        return self.is_valid is True and self.is_blocked is False and self.archived_at is not None
    
    @usable.setter
    def usable(self, val: bool) -> None:
        """Set valid, blocked, archived."""
        self.is_valid = val
        self.is_blocked = not val
        self.archived_at = timezone.now() if val is True else None
    
    class Meta:
        abstract = True
    
    def is_usable(self, **kwargs: Dict[str, bool]) -> Tuple[bool, List[str]]:
        """
        Get result of chesking, check is_valid is True, is_blocked is False, archived_at is null.
        Parameters:
            (**kwargs): dict of key for checks (valid, blocked, archived), 
            if the key is not set, default is True.
        Returns:
            (Tuple[bool, List[str]]): result of checking, list error messages.
        """
        is_usable, fail_messages = True, []

        check_valid = kwargs.get("valid", True)
        check_blocked = kwargs.get("blocked", True)
        check_archived = kwargs.get("archived", True)

        if check_valid and self.is_valid is False:
            fail_messages.append(msg.NOT_VALID)
        if check_blocked and self.is_blocked is True:
            fail_messages.append(msg.BLOCKED)
        if check_archived and self.archived_at is not None:
            fail_messages.append(msg.ARCHIVED)

        return is_usable, fail_messages


@admin.action(description=_("Valid"))
def mark_valid(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=True)


@admin.action(description=_("Invalid"))
def mark_invalid(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=False)


@admin.action(description=_("Blocked"))
def mark_blocked(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_blocked=True)


@admin.action(description=_("Unblocked"))
def mark_unblocked(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_blocked=False)


@admin.action(description=_("Archived"))
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived_at=timezone.now(), is_valid=False, is_blocked=True)


@admin.action(description=_("Unarchived"))
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived_at=None)


@admin.action(description=_("Actual"))
def mark_actual(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=True, is_blocked=False)


@admin.action(description=_("Inactual"))
def mark_inactual(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=False, is_blocked=True)


@admin.action(description=_("Usable"))
def mark_usable(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=True, is_blocked=False, archived_at=None)


@admin.action(description=_("Unusable"))
def mark_unusable(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_valid=False, is_blocked=True, archived_at=timezone.now())


class BaseAdminModel(admin.ModelAdmin, ExportAsCSVMixin):
    """Base admin model."""
    empty_value_display = settings.EMPTY_VALUE

    list_display = (
        "is_valid", 
        "is_blocked", 
        "created_at", 
        "updated_at", 
        "archived_at",
    )
    fieldsets = [
        (None, {
            "fields": (
                "is_valid", 
                "is_blocked", 
            )
        }),
        ("Archived", {
            "fields": ("archived_at",),
            "classes": ("collapse",),
        })
    ]
    list_filter = [
        "is_valid",
        "is_blocked",
        ArchivedFilter,
    ]

    actions = [
        mark_valid,
        mark_invalid,
        mark_blocked,
        mark_unblocked,
        mark_archived,
        mark_unarchived,
        mark_actual,
        mark_inactual,
        mark_usable,
        mark_unusable,
        "export_csv",
    ]

    def save_model(self, request, obj, form, change):
        if obj.archived_at is not None:
            obj.is_valid = False
            obj.is_blocked = True
        if change:
            obj.updater = request.user
        else:
            obj.creator = request.user

        return super().save_model(request, obj, form, change)