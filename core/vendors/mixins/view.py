from django.conf import settings
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin,
)


class ContextDataMixin(ContextMixin):
    """Get view context data mixin."""

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProtectViewMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Protect view mixin."""
    permission_required = []
    login_url = settings.LOGIN_URL