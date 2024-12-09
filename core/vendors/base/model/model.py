from django.db import models
from typing import (
    Tuple,
    List,
    Any,
)


class BaseModel(models.Model):
    """Base model."""
    is_valid = models.BooleanField(
        default=True
    )
    is_blocked = models.BooleanField(
        default=False
    )

    @property
    def actual(self) -> bool:
        """Check valid is True, blocked is False."""
        return self.is_valid and not self.is_blocked

    @actual.setter
    def actual(self, val: bool) -> None:
        """Set valid and blocked."""
        self.is_valid = val
        self.is_blocked = not val

    def is_useable(self, **kwargs: Any) -> Tuple[bool, List[str]]:
        """Check is valid and not blocked."""

        is_valid, messages = True, []

        valid = kwargs.get("is_valid", True)
        blocked = kwargs.get("is_blocked", True)

        if valid and self.is_valid is False:
            is_valid = False
            messages.append("Not valid")
        if  blocked and self.is_blocked is True:
            is_valid = False
            messages.append("Blocked")

        return is_valid, messages







