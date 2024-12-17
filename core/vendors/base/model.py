from django.db import models
from core.vendors import messages as msg
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
    
    def deleted(self, deleted: bool = True):
        return self.filter(deleted_at__isnull=deleted)
    
    def usable(self, valid: bool = True, blocked: bool = False, deleted: bool = False):
        return self.filter(is_valid=valid, is_blocked=blocked, deleted_at__isnull=not deleted)


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
    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    objects = BaseQuerySet.as_manager()

    @property
    def usable(self) -> bool:
        """Get check: is_valid is True and is_blocked is False and deleted_at is null."""
        return self.is_valid is True and self.is_blocked is False and self.deleted_at is not None
    
    class Meta:
        abstract = True
    
    def is_usable(self, **kwargs: Dict[str, bool]) -> Tuple[bool, List[str]]:
        """
        Get result of chesking, check is_valid is True, is_blocked is False, deleted_at is null.
        Parameters:
            (**kwargs): dict of key for checks (valid, blocked, deleted), 
            if the key is not set, default is True.
        Returns:
            (Tuple[bool, List[str]]): result of checking, list error messages.
        """
        is_usable, fail_messages = True, []

        check_valid = kwargs.get("valid", True)
        check_blocked = kwargs.get("blocked", True)
        check_deleted = kwargs.get("deleted", True)

        if check_valid and self.is_valid is False:
            fail_messages.append(msg.NOT_VALID)
        if check_blocked and self.is_blocked is True:
            fail_messages.append(msg.BLOCKED)
        if check_deleted and self.deleted_at is not None:
            fail_messages.append(msg.DELETED)

        return is_usable, fail_messages

