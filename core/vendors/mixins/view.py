from django.conf import settings
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


class ContextDataMixin(ContextMixin):
    """Get context data."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProtectViewMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Access control to view, authorization and permissions."""
    login_url = settings.LOGIN_URL
    permission_required = []