from django.db import models
from core.vendors.base.model import BaseModel
from django.utils.translation import gettext_lazy as _


class Page(BaseModel):
    """Page model."""
    slug = models.SlugField(
        unique=True
    )
    settings = models.JSONField(
        default=dict
    )

    class Meta:
        verbose_name =  _("Page")
        verbose_name_plural =  _("Pages")
        indexes = [
            models.Index(fields=["slug",]),
        ]
    
    def __str__(self):
        return self.slug