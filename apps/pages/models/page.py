from django.db import models
from core.vendors.base.model import BaseModel


class Page(BaseModel):
    """Page model."""
    url = models.URLField()
    settings = models.JSONField(
        default=dict
    )