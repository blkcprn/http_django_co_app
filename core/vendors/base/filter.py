from django.contrib import admin
from django.http import HttpRequest 
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _


class ArchivedFilter(admin.SimpleListFilter):
    """Archived filter."""
    title = _("Archived")

    parameter_name = "archived_at"

    def lookups(self, request: HttpRequest, model_admin: admin.ModelAdmin):
        return [
            ("yes", _("Yes")),
            ("no", _("No")),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet):
        if self.value() == "yes":
            return queryset.filter(archived_at__isnull=False)
        if self.value() == "no":
            return queryset.filter(archived_at__isnull=True)