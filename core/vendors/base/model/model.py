"""
Base model class.
"""

from django.db import models
from typing import (
    Tuple,
    List,
)


type Usable = Tuple[bool, List[str]]


class BaseModel(models.Model):
    
    is_valid = models.BooleanField()
    is_blocked = models.BooleanField()
    archived_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
 
    def is_usable(self, **kwargs) -> Usable:
        """
        Check, is_valid is True, is_blocked is False, 
        archived_at is null.
        """
        pass
