from ..models import Page
from django.contrib import admin
from core.vendors.base.model import BaseAdminModel


@admin.register(Page)
class AdminPageModel(BaseAdminModel):
    fieldsets = [
        *BaseAdminModel.fieldsets,
        (None, {
            "fields": ("url",)
        }),
        ("Settings", {
            "fields": ("settings",)
        })
    ]

